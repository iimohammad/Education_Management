from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import EducationalAssistant, Student, User
from accounts.models import Teacher, EducationalAssistant,Student
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import AccessToken
import redis
from celery import shared_task
from django.core.mail import send_mail
import random
import string
from config.settings import EMAIL_HOST
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'email', 'phone')
        extra_kwargs = {
            'phone_number': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class EducationalAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalAssistant
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 


class RequestTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

    def generate_token(self):
        token_length = 40
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(token_length))

    @shared_task
    def send_token_email(email, token):
        send_mail(
            'ChangePassword Token',
            f'Dear user,\nyour changepassword token is {token}',
            from_email=EMAIL_HOST,
            recipient_list=[email]
        )

    def validate(self, attrs):
        email = attrs['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError('User does not exist')

        token = self.generate_token()

        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        redis_client.set(token, email, ex=3600)  
        send_token_email_task = self.send_token_email.delay(email, token)

        return attrs
    

class ChangePasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate_token(self, value):
        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        email = redis_client.get(value)
        if email:
            return value
        else:
            raise serializers.ValidationError("Invalid or expired token")


    def save(self):
        token = self.validated_data['token']
        new_password = self.validated_data['new_password']
        email =self.redis_client.get(token)
        user = User.objects.get(email=email)

        user.password = make_password(new_password)
        user.save()





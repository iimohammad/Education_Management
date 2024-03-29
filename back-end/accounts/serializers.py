from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import EducationalAssistant, Student, User
from accounts.models import Teacher, EducationalAssistant,Student, User


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_image', 'address', 'phone']
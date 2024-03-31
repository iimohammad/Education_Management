from rest_framework import serializers

from accounts.models import Student, Teacher, User
from education.models import (
                    Department,
                    Major,
                    Semester,
                    Course,
                    SemesterCourse,
                    SemesterUnitSelection,
                    SemesterClass,
                    SemesterAddRemove,
                    SemesterExam,
                    SemesterEmergency,
                    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'user_number',
            'national_code',
            'birthday',
            'profile_image',
            'phone',
            'address',
            'gender']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name', 'department_code', 'year_established',
                  'department_location']


class SemesterUnitSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterUnitSelection
        fields = '__all__'


class SemesterClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterClass
        fields = '__all__'


class SemesterAddRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterAddRemove
        fields = '__all__'


class SemesterExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterExam
        fields = '__all__'


class SemesterEmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterEmergency
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    unit_selection_time_range = SemesterUnitSelectionSerializer()
    class_time_range = SemesterClassSerializer()
    add_remove_time_range = SemesterAddRemoveSerializer()
    exams_time_range = SemesterExamSerializer()
    emergency_removal_time_range = SemesterEmergencySerializer()

    class Meta:
        model = Semester
        fields = ['name', 'start_semester', 'end_semester',
                  'semester_type', 'unit_selection_time_range',
                  'class_time_range', 'add_remove_time_range', 'exams_time_range',
                  'emergency_removal_time_range']
    
    def create(self, validated_data):
        unit_selection_time_range_data = validated_data.pop('unit_selection_time_range')
        class_time_range_data = validated_data.pop('class_time_range')
        add_remove_time_range_data = validated_data.pop('add_remove_time_range')
        exams_time_range_data = validated_data.pop('exams_time_range')
        emergency_removal_time_range_data = validated_data.pop('emergency_removal_time_range')

        semester = Semester.objects.create(**validated_data)

        SemesterUnitSelection.objects.create(semester=semester, **unit_selection_time_range_data)
        SemesterClass.objects.create(semester=semester, **class_time_range_data)
        SemesterAddRemove.objects.create(semester=semester, **add_remove_time_range_data)
        SemesterExam.objects.create(semester=semester, **exams_time_range_data)
        SemesterEmergency.objects.create(semester=semester, **emergency_removal_time_range_data)

        return semester


class MajorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Major
        fields = ['major_name', 'major_code', 'department',
                  'number_of_credits', 'level', 'education_group']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    major = MajorSerializer()

    class Meta:
        model = Student
        fields = [
            'user',
            'entry_semester',
            'gpa',
            'entry_year',
            'major',
            'advisor',
            'military_service_status',
            'year_of_study',
            'major']


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'expertise', 'rank', 'department']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'department',
                  'major', 'credit_num']


class SemesterCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterCourse
        fields = ['semester', 'course', 'class_days', 'class_time_start',
                  'class_time_end', 'exam_datetime', 'exam_location',
                  'instructor', 'course_capacity', 'corse_reserve_capasity']
        
    def get_class_days(self, obj):
        
        return [day.name for day in obj.class_days.all()]

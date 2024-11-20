from rest_framework import serializers
from .models import Subject, Course, Module
from apps.instructors.serializers import InstructorSerializer
from apps.students.serializers import StudentSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseGETSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    instructor = InstructorSerializer()
    students = StudentSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

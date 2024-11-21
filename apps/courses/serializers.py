from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Subject, Course, Module
from core.utils.shared_serializers import GenericModelSerializer
from apps.instructors.models import Instructor


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseGETSerializer(serializers.ModelSerializer):
    subject = GenericModelSerializer(model=Subject)
    instructor = GenericModelSerializer(model=Instructor)
    students = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    modules = GenericModelSerializer(model=Module, many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_students(self, obj):
        request = self.context.get('request')
        return reverse('courses-students', args=[obj.id], request=request)

    def get_reviews(self, obj):
        request = self.context.get('request')
        return reverse('courses-reviews', args=[obj.id], request=request)


class ModuleSerializer(serializers.ModelSerializer):
    course = GenericModelSerializer(model=Course)

    class Meta:
        model = Module
        fields = '__all__'


class SingleSubjectSerializer(serializers.ModelSerializer):
    courses = GenericModelSerializer(model=Course, many=True)

    class Meta:
        model = Subject
        fields = '__all__'

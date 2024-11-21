from rest_framework import serializers
from core.utils.shared_serializers import GenericModelSerializer
from apps.students.models import Student
from .models import CourseReview


class CourseReviewSerializer(serializers.ModelSerializer):
    author = GenericModelSerializer(model=Student)

    class Meta:
        model = CourseReview
        exclude = ['course']

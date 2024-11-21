from rest_framework import serializers
from .models import CourseReview


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'

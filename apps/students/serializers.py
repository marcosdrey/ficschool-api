from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from core.utils.serializer_validators import is_name_valid
from core.utils.shared_serializers import GenericModelSerializer
from apps.courses.models import Course
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, value):
        if not is_name_valid(value):
            raise serializers.ValidationError(_('The name must have only letters and at least 4 characters'))
        return value


class SingleStudentSerializer(serializers.ModelSerializer):
    courses = GenericModelSerializer(model=Course, many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'birthday',
                  'cpf', 'email', 'phone_number',
                  'courses', 'created_at', 'updated_at']

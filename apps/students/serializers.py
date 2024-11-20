from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .validators import is_name_valid
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, value: str):
        if not is_name_valid(value):
            raise serializers.ValidationError(_('The name must have only letters and at least 4 characters'))
        return value

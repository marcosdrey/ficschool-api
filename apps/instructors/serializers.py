from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from core.utils.serializer_validators import is_name_valid
from .models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

    def validate_name(self, value):
        if not is_name_valid(value):
            raise serializers.ValidationError(_('The name must have only letters and at least 4 characters'))
        return value

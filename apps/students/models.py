import uuid
from django.db import models
from core.validators import MinAgeValidator, BRCPFValidator
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=300)
    birthday = models.DateField(validators=[MinAgeValidator(12)])
    cpf = models.CharField(unique=True, max_length=14, validators=[BRCPFValidator()])
    email = models.EmailField(max_length=500)
    phone_number = PhoneNumberField(max_length=30, unique=True, region='BR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

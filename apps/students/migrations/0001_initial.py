# Generated by Django 5.1.3 on 2024-11-19 17:41

import core.validators
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('birthday', models.DateField(validators=[core.validators.MinAgeValidator(12)])),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[core.validators.BRCPFValidator()])),
                ('email', models.EmailField(max_length=500)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=30, region='BR', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

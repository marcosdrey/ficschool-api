# Generated by Django 5.1.3 on 2024-11-19 19:39

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Worst possible rating is 1'), django.core.validators.MaxValueValidator(5, 'Best possible rating is 5')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='students.student')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='courses.course')),
            ],
            options={
                'ordering': ['course__name'],
                'constraints': [models.UniqueConstraint(fields=('author', 'course'), name='unique_review_course')],
            },
        ),
    ]
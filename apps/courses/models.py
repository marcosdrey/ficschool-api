import uuid
from django.db import models
from django.core.validators import MinValueValidator
from apps.instructors.models import Instructor
from apps.students.models import Student


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name='courses')
    students = models.ManyToManyField(Student, blank=True)
    workload = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', 'subject__name']

    def __str__(self):
        return self.name


class Module(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='modules')
    order = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', 'course__name']
        constraints = [
            models.UniqueConstraint(fields=['course', 'order'], name='unique_order_course')
        ]

    def __str__(self):
        return self.name

import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from apps.courses.models import Course
from apps.students.models import Student


class CourseReview(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[
        MinValueValidator(1, _('Worst possible rating is 1')),
        MaxValueValidator(5, _('Best possible rating is 5'))
    ])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['course__name']
        constraints = [
            models.UniqueConstraint(fields=['author', 'course'], name='unique_review_course')
        ]

    def __str__(self):
        return f'{self.author.name}: {self.course.name}'

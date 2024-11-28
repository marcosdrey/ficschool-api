from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CourseReview


@admin.register(CourseReview)
class CourseReviewAdmin(ModelAdmin):
    list_display = ('author__name', 'course__name', 'rating', 'created_at')
    search_fields = ('author__name', 'course__name')
    list_filter = ('rating',)

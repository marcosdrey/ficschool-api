from django.contrib import admin
from .models import CourseReview


@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('author__name', 'course__name', 'rating', 'created_at')
    search_fields = ('author__name', 'course__name')
    list_filter = ('rating',)

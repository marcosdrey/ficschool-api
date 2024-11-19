from django.contrib import admin
from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject__name', 'instructor__name', 'workload', 'show_total_students')
    list_display_links = ('name',)
    search_fields = ('name', 'subject__name', 'instructor__name')

    def show_total_students(self, obj):
        return obj.students.count()

    show_total_students.short_description = 'Total of Students'


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course__name', 'order', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name', 'course__name')

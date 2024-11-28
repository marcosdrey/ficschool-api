from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Student


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone_number', 'birthday')
    search_fields = ('name', 'cpf', 'email', 'phone_number')
    list_display_links = ('name',)

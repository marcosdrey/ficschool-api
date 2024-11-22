import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):

    birthday_gte = django_filters.DateFilter(field_name='birthday', lookup_expr='gte')
    birthday_lte = django_filters.DateFilter(field_name='birthday', lookup_expr='lte')
    birthday = django_filters.DateFilter(field_name='birthday')

    class Meta:
        model = Student
        fields = ('birthday_gte', 'birthday_lte', 'birthday')

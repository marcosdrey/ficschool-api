import django_filters
from .models import Instructor


class InstructorFilter(django_filters.FilterSet):

    birthday_gte = django_filters.DateFilter(field_name='birthday', lookup_expr='gte')
    birthday_lte = django_filters.DateFilter(field_name='birthday', lookup_expr='lte')
    birthday = django_filters.DateFilter(field_name='birthday')

    class Meta:
        model = Instructor
        fields = ('birthday_gte', 'birthday_lte', 'birthday')

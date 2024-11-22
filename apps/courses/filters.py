import django_filters
from .models import Course


class CourseFilter(django_filters.FilterSet):

    workload_gte = django_filters.NumberFilter(field_name='workload', lookup_expr='gte')
    workload_lte = django_filters.NumberFilter(field_name='workload', lookup_expr='lte')
    workload = django_filters.NumberFilter(field_name='workload')

    class Meta:
        model = Course
        fields = ('workload_gte', 'workload_lte', 'workload')

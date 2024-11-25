from rest_framework.viewsets import ModelViewSet
from .models import Course, Subject, Module
from . import serializers
from .filters import CourseFilter


class SubjectViewSet(ModelViewSet):
    """
    Complete CRUD viewset for the subjects.

    Accepts all HTTP requests.

    Search fields:
    - You can search (using 'search' parameter) by the name.

    Ordering fields:
    - You can order (using 'ordering' parameter) by any field you want
    """
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    search_fields = ['name']

    def get_serializer_class(self):
        return (
            serializers.SingleSubjectSerializer if
            self.action == 'retrieve' else
            super().get_serializer_class()
        )


class CourseViewSet(ModelViewSet):
    """
    Complete CRUD viewset for the courses.

    Accepts all HTTP requests.

    Search fields:
    - You can search (using 'search' parameter) by the name of: the course itself, the subject or the instructor related.

    Ordering fields:
    - You can order (using 'ordering' parameter) by any field you want (except workload)
    - To filter by the workload, you should use the 'workload' parameter, using the complement '_lte' to less than and equal values or '_gte' to greater than and equal values.
    """
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    search_fields = ['name', 'subject__name', 'instructor__name']
    filterset_class = CourseFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.CourseGETSerializer
        return super().get_serializer_class()


class ModuleViewSet(ModelViewSet):
    """
    Complete CRUD viewset for the modules.

    Accepts all HTTP requests.

    Search fields:
    - You can search (using 'search' parameter) by the name of: the module itself or the course related.

    Ordering fields:
    - You can order (using 'ordering' parameter) by any field you want
    """
    queryset = Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    search_fields = ['name', 'course__name']

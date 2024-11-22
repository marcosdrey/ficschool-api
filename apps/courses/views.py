from rest_framework.viewsets import ModelViewSet
from .models import Course, Subject, Module
from . import serializers
from .filters import CourseFilter


class SubjectViewSet(ModelViewSet):
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
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    search_fields = ['name', 'subject__name', 'instructor__name']
    filterset_class = CourseFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.CourseGETSerializer
        return super().get_serializer_class()


class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    search_fields = ['name', 'course__name']

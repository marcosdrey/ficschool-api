from rest_framework.viewsets import ModelViewSet
from .models import Course, Subject, Module
from . import serializers


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.CourseGETSerializer
        return super().get_serializer_class()


class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = serializers.ModuleSerializer

from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer, SingleStudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        return SingleStudentSerializer if self.action == 'retrieve' else super().get_serializer_class()


class StudentsByCourseListView(ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(courses__id=self.kwargs['course_id'])

from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer, SingleStudentSerializer
from .filters import StudentFilter


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = ['name', 'cpf', 'email', 'phone_number']
    filterset_class = StudentFilter

    def get_serializer_class(self):
        return (
            SingleStudentSerializer if
            self.action == 'retrieve' else
            super().get_serializer_class()
        )


class StudentsByCourseListView(ModelViewSet):
    serializer_class = StudentSerializer
    search_fields = ['name', 'cpf', 'email', 'phone_number']
    filterset_class = StudentFilter

    def get_queryset(self):
        return Student.objects.filter(courses__id=self.kwargs['course_id'])

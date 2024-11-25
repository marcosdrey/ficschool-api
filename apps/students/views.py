from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer, SingleStudentSerializer
from .filters import StudentFilter


class StudentViewSet(ModelViewSet):
    """
    Complete CRUD viewset for the students.

    Accepts all HTTP requests.

    Search fields:
    - You can search (using 'search' parameter) by: name, cpf, email or phone_number

    Ordering fields:
    - You can order (using 'ordering' parameter) by any field you want (except birthday)
    - To filter by the birthday, you should use the 'birthday' parameter, using the complement '_lte' to less than and equal values or '_gte' to greater than and equal values.
    """
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
    """
    List the students according to the course provided in the URL.

    Accepts only GET requests.

    Parameters:
    - course_id (uuid): The primary key of the course related to the students. Must be an UUID.

    Filters and ordering are the same to the normal Students route.
    """
    serializer_class = StudentSerializer
    search_fields = ['name', 'cpf', 'email', 'phone_number']
    filterset_class = StudentFilter

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        if course_id:
            return Student.objects.filter(courses__id=self.kwargs['course_id'])
        return Student.objects.none()

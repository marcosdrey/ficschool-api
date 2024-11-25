from rest_framework.viewsets import ModelViewSet
from .models import Instructor
from .serializers import InstructorSerializer, SingleInstructorSerializer
from .filters import InstructorFilter


class InstructorViewSet(ModelViewSet):
    """
    Complete CRUD viewset for the instructors.

    Accepts all HTTP requests.

    Search fields:
    - You can search (using 'search' parameter) by: name, cpf, email or phone_number

    Ordering fields:
    - You can order (using 'ordering' parameter) by any field you want (except birthday)
    - To filter by the birthday, you should use the 'birthday' parameter, using the complement '_lte' to less than and equal values or '_gte' to greater than and equal values.
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    search_fields = ['name', 'cpf', 'email', 'phone_number']
    filterset_class = InstructorFilter

    def get_serializer_class(self):
        return (
            SingleInstructorSerializer if
            self.action == 'retrieve' else
            super().get_serializer_class()
        )

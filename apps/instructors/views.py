from rest_framework.viewsets import ModelViewSet
from .models import Instructor
from .serializers import InstructorSerializer, SingleInstructorSerializer
from .filters import InstructorFilter


class InstructorViewSet(ModelViewSet):
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

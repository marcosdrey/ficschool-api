from rest_framework.viewsets import ModelViewSet
from .models import Instructor
from .serializers import InstructorSerializer, SingleInstructorSerializer


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get_serializer_class(self):
        return (
            SingleInstructorSerializer if
            self.action == 'retrieve' else
            super().get_serializer_class()
        )

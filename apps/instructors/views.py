from rest_framework.viewsets import ModelViewSet
from .models import Instructor
from .serializers import InstructorSerializer


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

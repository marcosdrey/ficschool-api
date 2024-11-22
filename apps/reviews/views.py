from rest_framework.viewsets import ModelViewSet
from .models import CourseReview
from .serializers import CourseReviewSerializer


class CourseReviewViewSet(ModelViewSet):
    serializer_class = CourseReviewSerializer

    def get_queryset(self):
        return CourseReview.objects.filter(course__id=self.kwargs['course_id'])

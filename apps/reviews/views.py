from rest_framework.viewsets import ModelViewSet
from .models import CourseReview
from .serializers import CourseReviewSerializer


class CourseReviewViewSet(ModelViewSet):
    """
    List the reviews according to the course provided in the URL.

    Accepts all HTTP requests.

    Parameters:
    - course_id (uuid): The primary key of the course related to the students. Must be an UUID.
    """
    serializer_class = CourseReviewSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        if course_id:
            return CourseReview.objects.filter(course__id=course_id)
        return CourseReview.objects.none()

from rest_framework.viewsets import ModelViewSet
from .models import CourseReview
from .serializers import CourseReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer

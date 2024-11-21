from django.urls import path
from . import views


urlpatterns = [
    path('courses/<uuid:course_id>/reviews/', views.CourseReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='courses-reviews'),
    path('courses/<uuid:course_id>/reviews/<uuid:pk>/', views.CourseReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='courses-reviews'),
]

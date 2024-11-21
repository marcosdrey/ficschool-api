from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('students', views.StudentViewSet, 'students')

urlpatterns = [
    path('', include(router.urls)),
    path('courses/<uuid:course_id>/students/', views.StudentsByCourseListView.as_view({'get': 'list'}), name='courses-students'),
]

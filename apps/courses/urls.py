from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('subjects', views.SubjectViewSet, 'subjects')
router.register('courses', views.CourseViewSet, 'courses')
router.register('modules', views.ModuleViewSet, 'modules')


urlpatterns = [
    path('', include(router.urls))
]

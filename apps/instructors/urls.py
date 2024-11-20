from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('instructors', views.InstructorViewSet, 'instructors')


urlpatterns = [
    path('', include(router.urls))
]

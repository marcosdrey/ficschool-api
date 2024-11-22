from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.students.urls')),
    path('api/v1/', include('apps.instructors.urls')),
    path('api/v1/', include('apps.courses.urls')),
    path('api/v1/', include('apps.reviews.urls')),

    path('api/v1/auth/', include('apps.authentication.urls'))
]

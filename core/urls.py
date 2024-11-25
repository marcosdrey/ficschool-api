from django.contrib import admin
from django.urls import path, include
from rest_framework.authentication import BasicAuthentication
from drf_yasg import views as swagger_views, openapi


schema_view = swagger_views.get_schema_view(
    openapi.Info(
        title="Ficticious School API",
        default_version='v1',
        description="API built for studying purposes of a ficticious school!",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License")
    ),
    authentication_classes=[BasicAuthentication]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.students.urls')),
    path('api/v1/', include('apps.instructors.urls')),
    path('api/v1/', include('apps.courses.urls')),
    path('api/v1/', include('apps.reviews.urls')),

    path('api/v1/auth/', include('apps.authentication.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

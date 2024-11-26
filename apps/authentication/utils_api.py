from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def obtain_superuser_client_for_api_test():
    user = User.objects.create_superuser(username='admin', password='admin')
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

    return (user, client)

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from apps.authentication.utils_api import obtain_superuser_client_for_api_test
from apps.students.models import Student
from .factories import StudentFactory


class ViewSetStudentsTestCase(APITestCase):
    def setUp(self):
        self.user, self.client = obtain_superuser_client_for_api_test()
        self.url = reverse('students-list')
        self.student = StudentFactory.create()

    def test_get_students_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        fields = ('name', 'birthday', 'cpf', 'email', 'phone_number')
        test_student = StudentFactory.build(
            cpf="857.116.460-60",
            phone_number="+55 51 98765-4321",
            email="test.student2@gmail.com"
        )
        data = {field: getattr(test_student, field) for field in fields}

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Student.objects.filter(cpf=test_student.cpf).exists())

    def test_get_student_retrieve(self):
        url = f'{self.url}{self.student.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_student(self):
        url = f'{self.url}{self.student.id}/'
        data_update = {"email": "test.student3@gmail.com"}
        response = self.client.patch(url, data_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Student.objects.get(pk=self.student.id).email, "test.student3@gmail.com")

    def test_delete_student(self):
        url = f'{self.url}{self.student.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(pk=self.student.id).exists())

import factory
from apps.students.models import Student


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    name = "Test Student"
    email = "test.student@gmail.com"
    cpf = "622.045.990-34"
    birthday = "2000-01-01"
    phone_number = "+55 11 98765-4321"

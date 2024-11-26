from django.test import TestCase
from .factories import StudentFactory
from apps.students.models import Student
from apps.students.serializers import StudentSerializer


class SerializerStudentTestCase(TestCase):
    def setUp(self):
        self.student = StudentFactory()
        self.student_serializer = StudentSerializer(instance=self.student)

    def test_verify_serialized_fields(self):
        data = self.student_serializer.data
        model_field_names = {field.name for field in Student._meta.get_fields() if field.concrete}
        self.assertEqual(set(data.keys()), model_field_names)

    def test_verify_serialized_values(self):
        data = self.student_serializer.data
        for field in data.keys():
            # Don't consider the fields that are interpreted as objects
            if field not in ('id', 'created_at', 'updated_at'):
                self.assertEqual(data.get(field), getattr(self.student, field))

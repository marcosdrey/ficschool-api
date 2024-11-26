from django.test import TestCase, TransactionTestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.utils import timezone
from apps.students.models import Student
from .factories import StudentFactory


class ModelStudentTestCase(TestCase):
    def setUp(self):
        self.student = StudentFactory()

    def test_object_is_saved_properly(self):
        self.assertIsInstance(self.student, Student)
        self.assertTrue(Student.objects.filter(cpf=self.student.cpf).exists())

    def test_verify_student_attributes(self):
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.email, "test.student@gmail.com")
        self.assertEqual(self.student.cpf, "622.045.990-34")
        self.assertEqual(self.student.birthday, "2000-01-01")
        self.assertEqual(self.student.phone_number, "+55 11 98765-4321")

    def test_invalid_name_too_long(self):
        student = StudentFactory.build(name="A" * 301)
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_invalid_email_format(self):
        student = StudentFactory.build(email="A")
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_invalid_email_too_long(self):
        student = StudentFactory.build(email="A@mail.com" * 51)
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_invalid_birthday(self):
        student = StudentFactory.build(birthday=timezone.now().strftime('%Y-%m-%d'))
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_invalid_cpf(self):
        student = StudentFactory.build(cpf="000.000.000-00")
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_invalid_phone_number(self):
        student = StudentFactory.build(phone_number="000000")
        with self.assertRaises(ValidationError):
            student.full_clean()


class ModelStudentUniqueConstraintTestCase(TransactionTestCase):
    def test_cpf_unique_constraint(self):
        # Here a different phone number is defined because it also has a unique restriction, so the value of the field is changed to ensure that the uniqueness validation error is related to the cpf.
        StudentFactory(phone_number="+55 11 98888-8888")
        with self.assertRaises(IntegrityError):
            StudentFactory(phone_number="+55 11 98888-8888")

    def test_phone_number_unique_constraint(self):
        # Different cpf is set due to the same reason of the method above.
        StudentFactory(cpf="690.679.280-62")
        with self.assertRaises(IntegrityError):
            StudentFactory(cpf="690.679.280-62")

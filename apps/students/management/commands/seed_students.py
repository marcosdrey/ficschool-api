from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker
from apps.students.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'num_items',
            type=int,
            help="How many students to create",
            choices=range(1, 100)
        )

    def handle(self, *args, **options):
        num_items = options['num_items']
        fake = Faker('pt_BR')
        all_students = []

        for i, _ in enumerate(range(num_items), start=1):
            name = fake.first_name() + " " + fake.last_name()
            cpf = fake.cpf()
            phone_number = fake.cellphone_number()
            email = ".".join(name.lower().split(" ")) + "@gmail.com"
            birthday = fake.date_of_birth(minimum_age=12, maximum_age=90)

            student = Student(
                name=name, cpf=cpf, phone_number=phone_number,
                email=email, birthday=birthday
            )
            all_students.append(student)
            self.stdout.write(self.style.SUCCESS(f"{i} student(s) prepared"))

        try:
            self.stdout.write(self.style.WARNING("Applying students to the database..."))
            Student.objects.bulk_create(all_students)
            self.stdout.write(self.style.SUCCESS("Students were created successfully!"))
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f"Error while creating students: {str(e)}"))

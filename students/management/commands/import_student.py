import csv
from django.core.management.base import BaseCommand, CommandError
from students.models import Student
import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv('PATH_TO_CSV_FILE')

class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help=path)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            with open(csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student, created = Student.objects.get_or_create(
                        register_no=row['register_no'],
                        defaults={
                            'name': row['name'],
                            'batch': row['batch'],
                            'degree': row['degree'],
                            'branch': row['branch'],
                            'On_Off_Campus': row['On_Off_Campus'],
                            'Company': row['Company'],
                            'Cost_To_Company': row['Cost_To_Company'],
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully created student {student.name}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Student {student.name} already exists'))

        except FileNotFoundError:
            raise CommandError(f'File "{csv_file}" does not exist')
        except KeyError as e:
            raise CommandError(f'CSV column missing: {e}')
        except Exception as e:
            raise CommandError(f'Error: {e}')

        self.stdout.write(self.style.SUCCESS('Successfully imported students'))


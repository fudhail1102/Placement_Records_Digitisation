# myapp/management/commands/delete_accepted_records.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Deletes records '

    def handle(self, *args, **options):
        print("working smooth")

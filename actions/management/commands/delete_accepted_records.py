# myapp/management/commands/delete_accepted_records.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from actions.models import Permission

class Command(BaseCommand):
    help = 'Deletes records with accepted status and acknowledged more than 24 hours ago.'

    def handle(self, *args, **options):
        queryset = Permission.objects.filter(status='A', acknowledged_time__lt=timezone.now() - timezone.timedelta(minutes=1))
        queryset.delete()

from django.core.management.base import BaseCommand, CommandError
from spells.models import Spell, ClassType
from spells.api import data_classes, class_entry

class Command(BaseCommand):
    '''Loop over the API classes and creates them within our db.'''
    def handle(self, *args, **options):
        class_entry(data_classes)
        self.stdout.write(self.style.SUCCESS('Successfully Populated Classes.'))
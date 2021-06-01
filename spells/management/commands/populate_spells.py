from django.core.management.base import BaseCommand, CommandError
from spells.models import Spell, ClassType
from spells.api import data_spells, spell_entry
import requests

base_url = 'https://www.dnd5eapi.co'


class Command(BaseCommand):
    ''' Loop over each spell for it's url, then use that url in a request to access
    all the other data in that individual spell. Once the data has been assigned
    to a variable, we create a new spell object and add classes '''
    def handle(self,  *args, **options):
        spell_entry(data_spells)
        self.stdout.write(self.style.SUCCESS('Successfully Populated Spells.'))
from django.core.management.base import BaseCommand, CommandError
from spells.models import Spell, ClassType
from spells.api import data_features, feature_entry
import requests

base_url = 'https://www.dnd5eapi.co'


class Command(BaseCommand):
    ''' Loop over every feature within the feature resource for its url. Then
    use the url to pull the neccesary data and create a new object. Features
    with no levels are set as 0 by default thanks to the try/except for KeyErrors'''
    def handle(self, *args, **options):
        feature_entry(data_features)
        self.stdout.write(self.style.SUCCESS('Successfully Populated Features.'))
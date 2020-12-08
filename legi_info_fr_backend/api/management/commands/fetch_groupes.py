from django.core.management.base import BaseCommand
import requests
from ...models.groupe import Groupe

def groupes():
    url = "https://www.nosdeputes.fr/organismes/groupe/json"
    result = requests.get(url)
    groupes = result.json()
    
    return groupes["organismes"]

def fill_groupes():
    for element in groupes():
        groupe = Groupe(
            slug=element["organisme"]["slug"],
            name=element["organisme"]["nom"],
            acronym=element["organisme"]["acronyme"],
            activeGroup=element["organisme"]["groupe_actuel"],
            rgbColor=element["organisme"]["couleur"],
        )
        groupe.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_groupes()
        print("--- Groups import COMPLETED ---")
import requests
from ...models.depute import Depute
from datetime import datetime
from django.core.management.base import BaseCommand

"""
Fetch all current deputies from NosDeputes API
"""
def deputes():
    url = "https://www.nosdeputes.fr/deputes/enmandat/json"
    result = requests.get(url)
    deputes = result.json()
    
    return deputes["deputes"]

def fill_deputes():
    date_format = "%Y-%m-%d"
    for element in deputes():
        depute = Depute(
            id=element["depute"]["id"],
            idAN=element["depute"]["id_an"],
            slug=element["depute"]["slug"],
            fullName=element["depute"]["nom"],
            firstName=element["depute"]["prenom"],
            lastName=element["depute"]["nom_de_famille"],
            birthDate=datetime.strptime(element["depute"]["date_naissance"], date_format).date(),
            birthPlace=element["depute"]["lieu_naissance"],
            departmentNumber=element["depute"]["num_deptmt"],
            districtName=element["depute"]["nom_circo"],
            districtNumber=element["depute"]["num_circo"],
            dateMandateStart=datetime.strptime(element["depute"]["mandat_debut"], date_format).date(),
            job=element["depute"]["profession"],
            otherMandates=element["depute"]["autres_mandats"],
        )
        depute.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_deputes()
        print("--- Deputies import COMPLETED ---")
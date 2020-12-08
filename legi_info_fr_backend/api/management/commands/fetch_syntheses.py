from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
import requests
from ...models.synthese import Synthese
from ...models.depute import Depute

def syntheses(date):
    url = "https://www.nosdeputes.fr/synthese/{}/json".format(date)
    result = requests.get(url)
    deputes = result.json()
    
    return deputes["deputes"]

def fill_syntheses():
    for annee in range(2018, 2021):
        for mois in range(1,13):
            for element in syntheses("201804"):
                try:
                    formatted_mois = ""
                    if mois < 10:
                        formatted_mois = "0{}".format(mois)
                    else:
                        formatted_mois = mois
                    date = "{}{}".format(annee, formatted_mois)
                    depute = Depute.objects.get(pk=element["depute"]["id"])
                    synthese = Synthese(
                        amendmentAdopted=element["depute"]["amendements_adoptes"],
                        amendmentProposed=element["depute"]["amendements_proposes"],
                        amendmentSigned=element["depute"]["amendements_signes"],
                        commissionIntervention=element["depute"]["commission_interventions"],
                        commissionAttendance=element["depute"]["commission_presences"],
                        hemicycleLongIntervention=element["depute"]["hemicycle_interventions"],
                        hemicycleShortIntervention=element["depute"]["hemicycle_interventions_courtes"],
                        propositionSigned=element["depute"]["propositions_signees"],
                        propositionWritten=element["depute"]["propositions_ecrites"],
                        questionWritten=element["depute"]["questions_ecrites"],
                        questionOral=element["depute"]["questions_orales"],
                        report=element["depute"]["rapports"],
                        weekAttendance=element["depute"]["semaines_presence"],
                        depute=depute,
                        date=date,
                    )
                    synthese.save()
                except ObjectDoesNotExist:
                    pass
            print("--- Synthese : {}/{} ---".format(mois, annee))

class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_syntheses()
        print("--- Syntheses import COMPLETED ---")
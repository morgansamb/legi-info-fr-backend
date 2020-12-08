from ...models.synthese import Synthese
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        Synthese.objects.all().delete()
        print("--- All synthesis DELETED ---")
from ...models.groupe import Groupe
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        Groupe.objects.all().delete()
        print("--- All groups DELETED ---")
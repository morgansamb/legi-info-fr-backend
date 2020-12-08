from ...models.depute import Depute
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        Depute.objects.all().delete()
        print("--- All deputies DELETED ---")
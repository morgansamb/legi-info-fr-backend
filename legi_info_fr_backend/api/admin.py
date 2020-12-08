from django.contrib import admin
from .models.depute import Depute
from .models.groupe import Groupe
from .models.synthese import Synthese

admin.site.register(Depute)
admin.site.register(Groupe)
admin.site.register(Synthese)

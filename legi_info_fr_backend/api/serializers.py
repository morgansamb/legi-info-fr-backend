from rest_framework import serializers
from .models.groupe import Groupe
from .models.depute import Depute
from .models.synthese import Synthese

class DeputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depute
        fields = '__all__'

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = '__all__'

class SyntheseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synthese
        exclude = ['depute']

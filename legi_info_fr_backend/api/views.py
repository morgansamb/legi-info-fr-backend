from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from .models import *

"""
Deputes endpoints
"""

@api_view(['GET'])
def deputeList(request):
    deputes = Depute.objects.all()
    serializer = DeputeSerializer(deputes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def syntheseByDepute(request, pk):
    syntheses = Synthese.objects.filter(depute_id=pk)
    serializer = SyntheseSerializer(syntheses, many=True)
    return Response(serializer.data)

"""
Groupes endpoints
"""

@api_view(['GET'])
def groupeList(request):
    groupes = Groupe.objects.all()
    serializer = GroupeSerializer(groupes, many=True)
    return Response(serializer.data)

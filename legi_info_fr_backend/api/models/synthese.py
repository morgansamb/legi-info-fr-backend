from django.db import models
from .depute import Depute

class Synthese(models.Model):
    id = models.IntegerField(primary_key=True)
    amendmentAdopted = models.IntegerField()
    amendmentProposed = models.IntegerField()
    amendmentSigned = models.IntegerField()
    commissionIntervention = models.IntegerField()
    commissionAttendance = models.IntegerField()
    hemicycleLongIntervention = models.IntegerField()
    hemicycleShortIntervention = models.IntegerField()
    propositionSigned = models.IntegerField()
    propositionWritten = models.IntegerField()
    questionWritten = models.IntegerField()
    questionOral = models.IntegerField()
    report = models.IntegerField()
    weekAttendance = models.IntegerField()
    # Synthesis linked to a Deputy
    depute = models.ForeignKey(Depute, on_delete=models.CASCADE)
    #Synthesis date
    date = models.CharField(max_length=124)
    
    def __str__(self):
        return "{}: {}".format(self.date, self.depute.fullName)

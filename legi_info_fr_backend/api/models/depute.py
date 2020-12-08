from django.db import models

def array_default():
    return []

class Depute(models.Model):
    id = models.IntegerField(primary_key=True)
    idAN = models.CharField(max_length=64)
    slug = models.CharField(max_length=256)
    fullName = models.CharField(max_length=256)
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    birthDate = models.DateField()
    birthPlace = models.CharField(max_length=256, null=True)
    departmentNumber = models.CharField(max_length=3)
    districtName = models.CharField(max_length=256)
    districtNumber = models.IntegerField()
    dateMandateStart = models.DateField()
    job = models.CharField(max_length=256, null=True)
    chamberPlace = models.CharField(max_length=4, default="")
    twitter = models.CharField(max_length=124, default="")
    numberOfMandates = models.IntegerField(default=1)
    otherMandates = models.JSONField("other_mandates", default=array_default)


    def __str__(self):
            return self.fullName
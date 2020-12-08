from django.db import models

class Groupe(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=256)
    name = models.CharField(max_length=524)
    acronym = models.CharField(max_length=8)
    activeGroup = models.BooleanField()
    rgbColor = models.CharField(max_length=12)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Iata(models.Model):
    iata_code = models.CharField(max_length=3,primary_key=True)
    lat = models.DecimalField(decimal_places=7,max_digits=15)
    lng = models.DecimalField(max_digits=15,decimal_places=7)

    def __str__(self):
        return self.iata_code

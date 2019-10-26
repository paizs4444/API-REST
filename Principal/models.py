from django.db import models

# Create your models here.
class PersonaMovil(models.Model):
    telefonoPer = models.CharField(primary_key=True,max_length=15)
    nombrePer = models.CharField(max_length=50)
    correoPer = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.nombrePer)

class AlertaPerona(models.Model):
    telefonoPer = models.CharField(max_length=15)
    nombrePer = models.CharField(max_length=50)
    correoPer = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    tipoAccidente = models.CharField(primary_key=True,max_length=50)

    def __str__(self):
        return "%s" % (self.nombrePer)

class Accidente(models.Model):
    Accidente = models.CharField(primary_key=True,max_length=15)

    def __str__(self):
        return "%s" % (self.Accidente)

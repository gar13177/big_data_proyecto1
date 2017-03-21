from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

class Tripulacion(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=200)
	base = models.CharField(max_length=200)

class Avion(models.Model):
	codigo = models.IntegerField()
	tipo = models.CharField(max_length=200)
	base = models.CharField(max_length=200)

class Piloto(models.Model):
	codigo = models.IntegerField()
	nombre =  models.CharField(max_length=200)
	horas_vuelo = models.DateTimeField()
	base = models.CharField(max_length=200)

class Vuelo(models.Model):
	fecha = models.DateField()
	origen = models.CharField(max_length=200)
	destino = models.CharField(max_length=200)
	hora = models.DateTimeField()
	tripulacion = ListField(EmbeddedModelField('Tripulacion'))
	avion = EmbeddedModelField('Avion')
	piloto = EmbeddedModelField('Piloto')

# Create your models here.

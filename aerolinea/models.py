from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField
from .nforms import ObjectListField, StringListField

class EmbedOverrideField(EmbeddedModelField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, ObjectListField, **kwargs)

class CategoryField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class Tripulacion(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=200)
	base = models.CharField(max_length=200)
	def __unicode__(self):
		return '%s %s' % (self.codigo, self.nombre, self.base)

class Avion(models.Model):
	codigo = models.IntegerField()
	tipo = models.CharField(max_length=200)
	base = models.CharField(max_length=200)
	def __unicode__(self):
		return '%s %s' % (self.codigo, self.tipo, self.base)

class Piloto(models.Model):
	codigo = models.IntegerField()
	nombre =  models.CharField(max_length=200)
	horas_vuelo = models.FloatField()
	base = models.CharField(max_length=200)
	def __unicode__(self):
		return '%s %s' % (self.codigo, self.nombre, self.horas_vuelo, self.base)

class Vuelo(models.Model):
	fecha = models.DateField()
	origen = models.CharField(max_length=200)
	destino = models.CharField(max_length=200)
	hora = models.TimeField()
	tripulacion = CategoryField()
	avion = EmbedOverrideField('Avion')
	piloto = EmbedOverrideField('Piloto')
	def __unicode__(self):
		return '%s %s (%s)' % (self.avion.codigo, self.piloto.codigo, self.tripulacion.codigo, self.fecha, self.origen, self.destino, self.hora)


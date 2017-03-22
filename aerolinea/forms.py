from django import forms

from aerolinea.models import Tripulacion, Piloto, Avion, Vuelo

class TripulacionForm(forms.ModelForm):
    class Meta:
        model = Tripulacion
        fields = ('codigo', 'nombre','base')

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = ('codigo', 'nombre','horas_vuelo', 'base')

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ('codigo', 'tipo', 'base')

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ('fecha', 'origen', 'destino', 'hora', 'tripulacion', 'avion','piloto')


class VueloForm2(forms.Form):
    fecha = forms.DateField()
    origen = forms.CharField(max_length=200)
    destino = forms.CharField(max_length=200)
    hora = forms.TimeField()
    tripulacion = forms.CharField(max_length=200)
    avion = forms.CharField(max_length=200)
    piloto = forms.CharField(max_length=200)
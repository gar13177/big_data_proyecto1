from django import forms

from aerolinea.models import Tripulacion

class TripulacionForm(forms.ModelForm):
    class Meta:
        model = Tripulacion
        fields = ('codigo', 'nombre','base')
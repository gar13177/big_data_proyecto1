from django.shortcuts import render

from aerolinea.models import Tripulacion
from aerolinea.forms import TripulacionForm

def tripulacion_index(request):

    tripulacion = Tripulacion.objects.all()
    print tripulacion

    return render(
        request,
        'tripulacion/index.html',
        {
            'tripulacion': tripulacion
        }
    )

def new_tripulacion(request):
    message = ''
    if request.method == 'GET':
        tripulacion_form = TripulacionForm()
    
    elif request.method == 'POST':
        tripulacion_form = TripulacionForm(data=request.POST)
        
        if tripulacion_form.is_valid():
            tripulacion_form.save()
            tripulacion_form = TripulacionForm()
            message = 'Tripulacion exitosamente guardada'

    
    return render(request,
     'tripulacion/new_tripulacion.html',
    { 
        'tripulacion_form': tripulacion_form,
        'message': message
    })

def tripulacion_detail(request, tripulacion_id):
    tripulacion = Tripulacion.objects.get(codigo=tripulacion_id)

    return render(
        request,
        'tripulacion/detail.html',
        {
            'tripulacion': tripulacion
        }
    )
from django.shortcuts import render

from aerolinea.models import Tripulacion, Piloto, Avion, Vuelo
from aerolinea.forms import TripulacionForm, PilotoForm, AvionForm, VueloForm


def new_vuelo(request):
    message = ''
    if request.method == 'GET':
        vuelo_form = VueloForm()
    
    elif request.method == 'POST':
        vuelo_form = VueloForm(data=request.POST)
        
        if vuelo_form.is_valid():
            vuelo_form.save()
            vuelo_form = VueloForm()
            message = 'Vuelo exitosamente guardado'

    
    return render(request,
     'vuelo/new.html',
    { 
        'vuelo_form': vuelo_form,
        'message': message
    })
def vuelo_detail(request, vuelo_id):
    vuelo = Vuelo.objects.get(id=vuelo_id)

    return render(
        request,
        'vuelo/detail.html',
        {
            'vuelo': vuelo
        }
    )

def vuelo_index(request):
    vuelos = Vuelo.objects.all()
    return render(
        request,
        'vuelo/index.html',
        {
            'vuelos':vuelos
        }
    )

def avion_index(request):
    aviones = Avion.objects.all()
    return render(
        request,
        'avion/index.html',
        {
            'aviones':aviones
        }
    )

def new_avion(request):
    message = ''
    if request.method == 'GET':
        avion_form = AvionForm()
    
    elif request.method == 'POST':
        avion_form = AvionForm(data=request.POST)
        
        if avion_form.is_valid():
            avion_form.save()
            avion_form = AvionForm()
            message = 'Avion exitosamente guardado'

    
    return render(request,
     'avion/new.html',
    { 
        'avion_form': avion_form,
        'message': message
    })

def avion_detail(request, avion_id):
    avion = Avion.objects.get(codigo=avion_id)

    return render(
        request,
        'avion/detail.html',
        {
            'avion': avion
        }
    )

def piloto_index(request):
    pilotos = Piloto.objects.all()
    return render(
        request,
        'piloto/index.html',
        {
            'pilotos': pilotos
        }
    )

def new_piloto(request):
    message = ''
    if request.method == 'GET':
        piloto_form = PilotoForm()
    
    elif request.method == 'POST':
        piloto_form = PilotoForm(data=request.POST)
        
        if piloto_form.is_valid():
            piloto_form.save()
            piloto_form = PilotoForm()
            message = 'Piloto exitosamente guardado'

    
    return render(request,
     'piloto/new.html',
    { 
        'piloto_form': piloto_form,
        'message': message
    })

def piloto_detail(request, piloto_id):
    piloto = Piloto.objects.get(codigo=piloto_id)

    return render(
        request,
        'piloto/detail.html',
        {
            'piloto': piloto
        }
    )


def tripulacion_index(request):

    tripulacion = Tripulacion.objects.all()

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
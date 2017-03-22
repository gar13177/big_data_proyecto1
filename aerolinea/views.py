from django.shortcuts import render

from aerolinea.models import Tripulacion, Piloto, Avion, Vuelo
from aerolinea.forms import TripulacionForm, PilotoForm, AvionForm, VueloForm2

def generic_index(request):
    return render(
        request,
        'generic/index.html',
        {}
    )

def new_vuelo(request):
    message = ''
    if request.method == 'GET':
        vuelo_form = VueloForm2()
    
    elif request.method == 'POST':
        vuelo_form = VueloForm2(request.POST)
        
        if vuelo_form.is_valid():
            
            fecha = vuelo_form.cleaned_data['fecha']
            origen = vuelo_form.cleaned_data['origen']
            destino = vuelo_form.cleaned_data['destino']
            hora = vuelo_form.cleaned_data['hora']
            tripulacion = vuelo_form.cleaned_data['tripulacion']
            tripList = tripulacion.split(',')
            tripInt = []
            for i in tripList:
                tripInt.append(int(i))
            avion = vuelo_form.cleaned_data['avion']
            avionInt = int(avion)
            piloto = vuelo_form.cleaned_data['piloto']
            pilotoInt = int(piloto)
            avion= Avion.objects.get(codigo = avionInt)
            piloto = Piloto.objects.get(codigo = pilotoInt)
            Vuelo(fecha=fecha,
                origen = origen, 
                destino = destino, 
                hora= hora,
                tripulacion = tripInt,
                avion = avion,
                piloto = piloto
                ).save()
            vuelo_form = VueloForm2()
            message = 'Vuelo exitosamente guardado'
    return render(request,
     'vuelo/new.html',
    { 
        'vuelo_form': vuelo_form,
        'message': message
    })

def edit_vuelo(request, vuelo_id):
    vuelo_form = VueloForm2(request.POST)
    message = ''
    #vuelo = Vuelo.objects.get(id=vuelo_id)
    if vuelo_form.is_valid():
        fecha = vuelo_form.cleaned_data['fecha']
        origen = vuelo_form.cleaned_data['origen']
        destino = vuelo_form.cleaned_data['destino']
        hora = vuelo_form.cleaned_data['hora']
        tripulacion = vuelo_form.cleaned_data['tripulacion']
        tripList = tripulacion.split(',')
        tripInt = []
        for i in tripList:
            tripInt.append(int(i))
        avion = vuelo_form.cleaned_data['avion']
        avionInt = int(avion)
        piloto = vuelo_form.cleaned_data['piloto']
        pilotoInt = int(piloto)
        avion= Avion.objects.get(codigo = avionInt)
        piloto = Piloto.objects.get(codigo = pilotoInt)
        Vuelo(id = vuelo_id,
        fecha=fecha,
        origen = origen, 
        destino = destino, 
        hora= hora,
        tripulacion = tripInt,
        avion = avion,
        piloto = piloto
        ).save()
        
        vuelo_form = VueloForm2()
        message = 'Vuelo exitosamente editado'
        
    return render(request,
     'vuelo/new.html',
    { 
        'vuelo_form': vuelo_form,
        'message': message
    })

def vuelo_delete(request, vuelo_id):
    vuelo = Vuelo.objects.get(id=vuelo_id)
    vuelo.delete()
    return vuelo_index(request)

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

def edit_avion(request, avion_id):
    avion = Avion.objects.get(id=avion_id)
    avion_form = AvionForm(request.POST or None, instance=avion)
    message = ''       
    if avion_form.is_valid():
        avion_form.save()
        message = 'Avion exitosamente guardado'
    
    return render(request,
     'avion/new.html',
    { 
        'avion_form': avion_form,
        'message': message
    })

def avion_delete(request, avion_id):
    avion = Avion.objects.get(id=avion_id)
    avion.delete()
    return avion_index(request)

def avion_detail(request, avion_id):
    avion = Avion.objects.get(id=avion_id)

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

def edit_piloto(request, piloto_id):
    piloto = Piloto.objects.get(id=piloto_id)
    piloto_form = PilotoForm(request.POST or None, instance=piloto)
    message = ''       
    if piloto_form.is_valid():
        piloto_form.save()
        message = 'Piloto exitosamente guardado'
    
    return render(request,
     'piloto/new.html',
    { 
        'piloto_form': piloto_form,
        'message': message
    })

def piloto_detail(request, piloto_id):
    piloto = Piloto.objects.get(id=piloto_id)

    return render(
        request,
        'piloto/detail.html',
        {
            'piloto': piloto
        }
    )
def piloto_delete(request, piloto_id):
    piloto = Piloto.objects.get(id=piloto_id)
    piloto.delete()
    return piloto_index(request)

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

def edit_tripulacion(request, tripulacion_id):
    tripulacion = Tripulacion.objects.get(id=tripulacion_id)
    tripulacion_form = TripulacionForm(request.POST or None, instance=tripulacion)
    message = ''       
    if tripulacion_form.is_valid():
        tripulacion_form.save()
        message = 'Tripulacion exitosamente guardada'
    
    return render(request,
     'tripulacion/new_tripulacion.html',
    { 
        'tripulacion_form': tripulacion_form,
        'message': message
    })

def tripulacion_detail(request, tripulacion_id):
    tripulacion = Tripulacion.objects.get(id=tripulacion_id)

    return render(
        request,
        'tripulacion/detail.html',
        {
            'tripulacion': tripulacion
        }
    )

def tripulacion_delete(request, tripulacion_id):
    tripulacion = Tripulacion.objects.get(id=tripulacion_id)
    tripulacion.delete()
    return tripulacion_index(request)
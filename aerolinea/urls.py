from django.conf.urls import url
from aerolinea import views as aerolinea_views

urlpatterns = [
    url(
        r'^tripulacion/$',
        aerolinea_views.tripulacion_index,
        name='tripulacion_index'),

    url(
        r'^tripulacion/new/$',aerolinea_views.new_tripulacion,
        name='tripulacion_new_tripulacion'),

    url(
        r'^tripulacion/detail/(?P<tripulacion_id>[0-9]+)/$',
        aerolinea_views.tripulacion_detail,
        name='tripulacion_tripulacion_detail'),

    url(
        r'^piloto/$',
        aerolinea_views.piloto_index,
        name='piloto_index'),

    url(
        r'^piloto/new/$',aerolinea_views.new_piloto,
        name='piloto_new_piloto'),

    url(
        r'^piloto/detail/(?P<piloto_id>[0-9]+)/$',
        aerolinea_views.piloto_detail,
        name='piloto_piloto_detail'),

    url(
        r'^avion/$',
        aerolinea_views.avion_index,
        name='avion_index'),

    url(
        r'^avion/new/$',aerolinea_views.new_avion,
        name='avion_new_avion'),

    url(
        r'^avion/detail/(?P<avion_id>[0-9]+)/$',
        aerolinea_views.avion_detail,
        name='avion_avion_detail'),

    url(
        r'^vuelo/$',
        aerolinea_views.vuelo_index,
        name='vuelo_index'),
    
    url(
        r'^vuelo/detail/(?P<vuelo_id>([0-9]|[a-z])+)/$',
        aerolinea_views.vuelo_detail,
        name='vuelo_vuelo_detail'),    

    url(
        r'^vuelo/new/$',aerolinea_views.new_vuelo,
        name='vuelo_new_vuelo'),   
        
]

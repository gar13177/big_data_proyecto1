from django.conf.urls import url
from aerolinea import views as aerolinea_views

urlpatterns = [
    url(
        r'^$',
        aerolinea_views.generic_index,
        name='generic_index'),
    
    url(
        r'^tripulacion/$',
        aerolinea_views.tripulacion_index,
        name='tripulacion_index'),

    url(
        r'^tripulacion/new/$',aerolinea_views.new_tripulacion,
        name='tripulacion_new_tripulacion'),

    url(
        r'^tripulacion/detail/(?P<tripulacion_id>[a-z\d]+)/$',
        aerolinea_views.tripulacion_detail,
        name='tripulacion_tripulacion_detail'),

    url(
        r'^tripulacion/delete/(?P<tripulacion_id>[a-z\d]+)/$',
        aerolinea_views.tripulacion_delete,
        name='tripulacion_tripulacion_delete'),

    url(
        r'^tripulacion/edit/(?P<tripulacion_id>[a-z\d]+)/$',
        aerolinea_views.edit_tripulacion,
        name='tripulacion_edit_tripulacion'),

    url(
        r'^piloto/$',
        aerolinea_views.piloto_index,
        name='piloto_index'),

    url(
        r'^piloto/new/$',aerolinea_views.new_piloto,
        name='piloto_new_piloto'),

    url(
        r'^piloto/detail/(?P<piloto_id>[a-z\d]+)/$',
        aerolinea_views.piloto_detail,
        name='piloto_piloto_detail'),

    url(
        r'^piloto/delete/(?P<piloto_id>[a-z\d]+)/$',
        aerolinea_views.piloto_delete,
        name='piloto_piloto_delete'),
    
    url(
        r'^piloto/edit/(?P<piloto_id>[a-z\d]+)/$',
        aerolinea_views.edit_piloto,
        name='piloto_edit_piloto'),

    url(
        r'^avion/$',
        aerolinea_views.avion_index,
        name='avion_index'),

    url(
        r'^avion/new/$',aerolinea_views.new_avion,
        name='avion_new_avion'),

    url(
        r'^avion/detail/(?P<avion_id>[a-z\d]+)/$',
        aerolinea_views.avion_detail,
        name='avion_avion_detail'),
    
    url(
        r'^avion/delete/(?P<avion_id>[a-z\d]+)/$',
        aerolinea_views.avion_delete,
        name='avion_avion_delete'),

    url(
        r'^avion/edit/(?P<avion_id>[a-z\d]+)/$',
        aerolinea_views.edit_avion,
        name='avion_edit_avion'),

    url(
        r'^vuelo/$',
        aerolinea_views.vuelo_index,
        name='vuelo_index'),
    
    url(
        r'^vuelo/detail/(?P<vuelo_id>[a-z\d]+)$',
        aerolinea_views.vuelo_detail,
        name='vuelo_vuelo_detail'),    

    url(
        r'^vuelo/new/$',aerolinea_views.new_vuelo,
        name='vuelo_new_vuelo'),

    url(
        r'^vuelo/delete/(?P<vuelo_id>[a-z\d]+)$',
        aerolinea_views.vuelo_delete,
        name='vuelo_vuelo_delete'),  

     url(
        r'^vuelo/edit/(?P<vuelo_id>[a-z\d]+)$',
        aerolinea_views.edit_vuelo,
        name='vuelo_edit_vuelo'),  
           
        
]

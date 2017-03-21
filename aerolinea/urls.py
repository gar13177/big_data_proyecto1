from django.conf.urls import url
from aerolinea import views as aerolinea_views

urlpatterns = [
    url(
        r'^$',
        aerolinea_views.tripulacion_index,
        name='tripulacion_index'),
        url(r'^tripulacion/new/$',aerolinea_views.new_tripulacion,
        name='tripulacion_new_tripulacion'),
        url(
        r'^tripulacion/detail/(?P<tripulacion_id>[0-9]+)/$',
        aerolinea_views.tripulacion_detail,
        name='tripulacion_tripulacion_detail'),
]

from django.conf.urls import url, patterns
from django.conf import settings
from clasificacion import views

urlpatterns = patterns('',
    url(r'^$', views.vistaClasificacion, name='vistaClasificacion'),
)

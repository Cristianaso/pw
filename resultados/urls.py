from django.conf.urls import url, patterns
from django.conf import settings
from resultados import views

urlpatterns = patterns('',
		url(r'^$', views.vistaResultados, name='vistaResultados'),
)

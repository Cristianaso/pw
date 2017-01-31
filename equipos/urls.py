from django.conf.urls import url, patterns
from django.conf import settings
from equipos import views

urlpatterns = patterns('',    
		url(r'^$', views.vistaEquipo, name='vistaEquipo'),
)

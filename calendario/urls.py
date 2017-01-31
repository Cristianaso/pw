from django.conf.urls import url, patterns
from django.conf import settings
from calendario import views

urlpatterns = patterns('',
		url(r'^$', views.vistaCalendario, name='vistaCalendario'),
)

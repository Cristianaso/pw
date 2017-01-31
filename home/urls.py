from django.conf.urls import url, patterns
from django.conf import settings
from home import views

urlpatterns = patterns('',
		url(r'^$', views.vistaHome, name='vistaHome'),
)

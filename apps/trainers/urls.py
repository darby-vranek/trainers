from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^doubles/$', views.doubles),
    url(r'^admin/', admin.site.urls),
	url(r'^trainer/([0-9]+)/$', views.show_trainer)
]

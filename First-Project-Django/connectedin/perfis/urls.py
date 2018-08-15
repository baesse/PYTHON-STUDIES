from django.conf.urls import include, url
from django.contrib import admin
from perfis import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^perfil/(?P<perfil_id>\d+)$',views.show,name='show'),
    url(r'^perfil/(?P<perfil_id>\d+)/invite$',views.invite,name='invite')
]

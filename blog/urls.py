from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SetIndexBackroundImg,name='index'),
    url(r'^spec/',views.spec,name='spec'),
    url(r'^contact/',views.contact,name='contact'),
]
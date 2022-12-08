from django.urls import path 

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('', views.cars, name='cars'),
    path('', views.services, name='services'),
    path('', views.contact, name='contact'),
]
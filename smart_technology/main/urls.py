from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),  # Page d'accueil
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),  # Page "Qui sommes-nous"
    path('services/', views.services, name='services'),  # Page "Nos services"
    path('contact/', views.contact, name='contact'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.livre_list),
    path('dvds/', views.dvd_list, name='dvd_list'),
    path('cds/', views.cd_list, name='cd_list'),
    path('jeux/', views.jeu_list, name='jeu_list'),
    path('emprunteurs/', views.emprunteur_list, name='emprunteur_list'),
]


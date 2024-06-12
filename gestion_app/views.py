from django.shortcuts import render
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur

def livre_list(request):
    livres = Livre.objects.all()
    return render(request, 'gestion_app/livre_list.html', {'livres': livres})

def dvd_list(request):
    dvds = DVD.objects.all()
    return render(request, 'gestion_app/dvd_list.html', {'dvds': dvds})

def cd_list(request):
    cds = CD.objects.all()
    return render(request, 'gestion_app/cd_list.html', {'cds': cds})

def jeu_list(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'gestion_app/jeu_list.html', {'jeux': jeux})

def emprunteur_list(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'gestion_app/emprunteur_list.html', {'emprunteurs': emprunteurs})

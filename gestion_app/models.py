from django.db import models

class Livre(models.Model):
    name = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.CharField(max_length=100, null=True, blank=True)

class DVD(models.Model):
    name = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.CharField(max_length=100, null=True, blank=True)

class CD(models.Model):
    name = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    dateEmprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.CharField(max_length=100, null=True, blank=True)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

class Emprunteur(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)



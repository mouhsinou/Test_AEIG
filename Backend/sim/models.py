# models.py
from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    createur = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True, blank=True)
    est_terminee = models.BooleanField(default=False)
    utilisateurs = models.ManyToManyField(User, related_name='taches')

    def __str__(self):
        return self.titre

class Permission(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    peut_ajouter_tache = models.BooleanField(default=False)
    peut_modifier_tache = models.BooleanField(default=False)
    peut_supprimer_tache = models.BooleanField(default=False)
    peut_marquer_tache_terminee = models.BooleanField(default=False)

    def __str__(self):
        return f'Permissions de {self.utilisateur.username}'

from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)  # Nom du service
    description = models.TextField()  # Description détaillée
    icon = models.CharField(max_length=50)  # Icône CSS ou chemin d'image

    def _str_(self):
        return self.name
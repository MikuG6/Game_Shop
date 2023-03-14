from django.db import models
from 

class Game(models.Model):
    name = models.CharField(max_length=50)
    discriprion = models.TextField()
    data_create = models.DataField()
    picture = models.ImageField(blank=True)
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        )

    def __str__(self):
        return self.name


class GanreGame(models.Model):
    ganre = models.CharField(max_length=50)

    def __str__(self):
        return self.ganre

class GameDevelopers(models.Model):
    ganre = models.CharField(max_length=50)

    def __str__(self):
        return self.ganre
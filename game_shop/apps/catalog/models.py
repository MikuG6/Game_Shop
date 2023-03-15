from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=50)
    discriprion = models.TextField()
    data_create = models.DateField()
    picture = models.ImageField(blank=True)
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        )
    game_devel = models.ForeignKey(
        "GameDevelopers",
        on_delete=models.CASCADE,
    )
    games = models.ManyToManyField(
        "GanreGame",
        db_table="games_ganre",
    )

    def __str__(self):
        return self.name


class GanreGame(models.Model):
    ganre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ganre


class GameDevelopers(models.Model):
    game_dev = models.CharField(max_length=50)
    
    def __str__(self):
        return self.game_dev
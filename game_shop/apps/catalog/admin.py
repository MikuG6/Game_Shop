from django.contrib import admin

from .models import Game, GameDevelopers, GanreGame
 
admin.site.register(Game)
admin.site.register(GameDevelopers)
admin.site.register(GanreGame)
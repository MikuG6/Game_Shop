from rest_framework import serializers
from .models import Game, GanreGame


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GanreGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GanreGame
        fields = ("ganre",)
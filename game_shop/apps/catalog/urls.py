from django.urls import path
from .views import GameAPIList

urlpatterns = [
    path("", GameAPIList.as_view(), name="game_list"),
]

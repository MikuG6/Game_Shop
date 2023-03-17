from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GameAPIListCreateView, GameAPIDetailView, GanreListCreateAPIView


router = DefaultRouter()

router.register(r'ganre', GanreListCreateAPIView)

urlpatterns = [
    path("", GameAPIListCreateView.as_view(), name="games_list"),
    path("<int:pk>/", GameAPIDetailView.as_view(), name="game"),
    path("", include(router.urls)),
]

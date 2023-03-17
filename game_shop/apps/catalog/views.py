from django.shortcuts import render
from rest_framework import generics, mixins, viewsets, pagination

from .models import Game, GanreGame
from .serializers import GameSerializer, GanreGameSerializer
from .permissions import IsAdminOrReadOnly


class GameAPIListPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class GameAPIListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = GameAPIListPagination


class GameAPIDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminOrReadOnly, )


class GanreListCreateAPIView(viewsets.GenericViewSet,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             mixins.ListModelMixin):
    queryset = GanreGame.objects.all()
    serializer_class = GanreGameSerializer
    permission_classes = (IsAdminOrReadOnly, )

from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from rest_framework import generics

from .models import User, BuyGame, PurchaseHistory
from .serializers import UserProfileSerializer, BuyGameSerializer, HistorySerializer
from .services import make_buy, create_history, make_history

from apps.catalog.models import Game
from apps.catalog.serializers import GameSerializer
from apps.catalog.views import GameAPIListPagination


class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserProfileSerializer


class BuyGameViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    queryset = BuyGame.objects.all()
    serializer_class = BuyGameSerializer
    permission_classes = (IsAuthenticated, )
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            try:
                history = create_history(**serializer.validated_data)
                make_buy(**serializer.validated_data)
                make_history(history=history, **serializer.validated_data)
            except ValueError:
                content = {'error': 'Not enough money'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)


class PurchaseHistoryListAPIView(generics.ListAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = HistorySerializer
    pagination_class = GameAPIListPagination

    # def get_queryset(self):
    #     accounts = User.objects.filter(user=self.request.user)
    #     return self.queryset.filter(account__in=accounts)
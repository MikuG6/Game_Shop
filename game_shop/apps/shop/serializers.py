from rest_framework import serializers

from .models import User, BuyGame, PurchaseHistory


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "balance", "email", )


class BuyGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyGame
        fields = ("who_buy", "what_buy", )


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        exclude = ("id", )


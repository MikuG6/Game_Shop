from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import UserProfileAPIView, BuyGameViewSet, PurchaseHistoryListAPIView


router = DefaultRouter()

router.register(r'buy_game', BuyGameViewSet)


urlpatterns = [
    path(
        "user_profile/<int:pk>/", 
        UserProfileAPIView.as_view(), 
        name="profile_user",
    ),
    path(
        "user_profile/<int:pk>/history/", 
        PurchaseHistoryListAPIView.as_view(), 
        name="history",
    ),
    path('', include(router.urls)),
]

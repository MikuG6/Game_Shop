from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# get_user_model() == request.user

class User(AbstractUser):
    balance = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        )

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'user': self.username})


class PurchaseHistory(models.Model):
    date_purchase = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owner',
        default=None,
    )
    purchase_price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
    )
    name = models.CharField(
        max_length=50,
        blank=True,
    )



class BuyGame(models.Model):
    who_buy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='who_buy'
    )
    what_buy = models.ForeignKey(
        "catalog.Game",
        on_delete=models.CASCADE,
        related_name='what_buy'
    )
    history = models.ForeignKey(
        PurchaseHistory,
        on_delete=models.CASCADE,
        related_name='history',
        default=None
    )
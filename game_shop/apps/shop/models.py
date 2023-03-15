from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# get_user_model() == request.user

class User(AbstractUser):
    money = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        )

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'user': self.username})

class PurchaseHistory(models.Model):
    date_purchase = models.DateTimeField(auto_now_add=True)
    # purchased_game = models.ForeignKey(
    #     "catalog.Game",
    #     on_delete=models.CASCADE,
    # )
    purchase_price = models.OneToOneField(
        "catalog.Game",
        on_delete=models.CASCADE,
    )
    who_buy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="User",
        on_delete=models.CASCADE,
    )
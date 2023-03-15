# Generated by Django 4.1.7 on 2023-03-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchasehistory",
            name="who_buy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="money",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]

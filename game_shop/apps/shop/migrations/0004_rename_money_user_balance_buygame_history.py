# Generated by Django 4.1.7 on 2023-03-16 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_alter_purchasehistory_who_buy_alter_user_money_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="money",
            new_name="balance",
        ),
        migrations.AddField(
            model_name="buygame",
            name="history",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="history",
                to="shop.purchasehistory",
            ),
        ),
    ]

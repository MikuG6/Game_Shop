# Generated by Django 4.1.7 on 2023-03-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ganregame",
            name="games",
        ),
        migrations.AddField(
            model_name="game",
            name="games",
            field=models.ManyToManyField(
                db_table="games_ganre", to="catalog.ganregame"
            ),
        ),
    ]

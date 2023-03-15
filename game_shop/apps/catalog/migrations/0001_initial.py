# Generated by Django 4.1.7 on 2023-03-14 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("discriprion", models.TextField()),
                ("data_create", models.DateField()),
                ("picture", models.ImageField(blank=True, upload_to="")),
                ("price", models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name="GameDevelopers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_dev", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="GanreGame",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ganre", models.CharField(max_length=50)),
                (
                    "games",
                    models.ManyToManyField(db_table="games_ganre", to="catalog.game"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="game_devel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="catalog.gamedevelopers"
            ),
        ),
    ]
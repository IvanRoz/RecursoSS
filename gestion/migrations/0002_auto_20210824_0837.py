# Generated by Django 3.2.6 on 2021-08-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subunit",
            options={"ordering": ("order",)},
        ),
        migrations.AlterField(
            model_name="subunit",
            name="order",
            field=models.PositiveIntegerField(
                help_text="Índice de la unidad (usado para ordenar cada unidad).", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="unit",
            name="order",
            field=models.PositiveIntegerField(
                help_text="Índice de la unidad (usado para ordenar cada unidad).", unique=True
            ),
        ),
    ]

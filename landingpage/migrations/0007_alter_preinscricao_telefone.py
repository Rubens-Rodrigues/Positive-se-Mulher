# Generated by Django 5.0.1 on 2024-01-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landingpage", "0006_alter_preinscricao_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preinscricao",
            name="telefone",
            field=models.CharField(max_length=15),
        ),
    ]

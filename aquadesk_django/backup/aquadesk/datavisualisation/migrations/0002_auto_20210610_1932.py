# Generated by Django 3.2.2 on 2021-06-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datavisualisation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countsession',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lifeform',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='size_weight_data',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='size_weight_model',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tank',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]
# Generated by Django 3.2 on 2021-12-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20211119_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='losses',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='wins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
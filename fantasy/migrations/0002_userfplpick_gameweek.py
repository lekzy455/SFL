# Generated by Django 3.2 on 2021-11-29 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20211119_1312'),
        ('fantasy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfplpick',
            name='gameweek',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='league.gameweekname'),
        ),
    ]

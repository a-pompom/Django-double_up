# Generated by Django 2.2.2 on 2019-11-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_gamestatus_gainedcoin'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestatus',
            name='currentMark',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamestatus',
            name='targetMark',
            field=models.IntegerField(default=0),
        ),
    ]
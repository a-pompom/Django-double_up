# Generated by Django 2.2.2 on 2019-11-03 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20191103_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestatus',
            name='gainedCoin',
            field=models.IntegerField(default=0),
        ),
    ]

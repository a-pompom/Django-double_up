# Generated by Django 2.2.2 on 2019-11-03 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20191027_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestatus',
            name='coin',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamestatus',
            name='doubleUpCount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.2 on 2019-10-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestatus',
            name='current',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamestatus',
            name='target',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

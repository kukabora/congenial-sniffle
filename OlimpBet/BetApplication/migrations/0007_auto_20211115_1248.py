# Generated by Django 3.2.8 on 2021-11-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetApplication', '0006_auto_20211114_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='coefficient',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='bet',
            name='potential',
            field=models.FloatField(default=1.0),
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-01 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BetApplication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='category',
        ),
        migrations.AddField(
            model_name='match',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='BetApplication.category'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.6 on 2022-09-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_admin',
            field=models.BooleanField(default=False),
        ),
    ]

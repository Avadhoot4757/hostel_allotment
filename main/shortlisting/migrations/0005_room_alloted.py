# Generated by Django 5.0.2 on 2024-04-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlisting', '0004_auto_20240404_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='alloted',
            field=models.BooleanField(default=False),
        ),
    ]

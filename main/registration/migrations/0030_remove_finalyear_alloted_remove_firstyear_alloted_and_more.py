# Generated by Django 5.0.2 on 2024-04-05 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0029_finalyear_alloted_firstyear_alloted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finalyear',
            name='alloted',
        ),
        migrations.RemoveField(
            model_name='firstyear',
            name='alloted',
        ),
        migrations.RemoveField(
            model_name='secondyear',
            name='alloted',
        ),
        migrations.RemoveField(
            model_name='thirdyear',
            name='alloted',
        ),
    ]

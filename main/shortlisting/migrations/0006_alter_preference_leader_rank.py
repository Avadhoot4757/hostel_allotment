# Generated by Django 3.2.18 on 2024-04-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlisting', '0005_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='leader_rank',
            field=models.IntegerField(),
        ),
    ]

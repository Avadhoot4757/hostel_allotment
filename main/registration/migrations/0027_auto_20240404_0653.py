# Generated by Django 3.2.18 on 2024-04-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0026_alter_secondyear_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalyear',
            name='rank',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='thirdyear',
            name='rank',
            field=models.FloatField(),
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlisting', '0003_auto_20240312_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

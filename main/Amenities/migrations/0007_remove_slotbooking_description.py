# Generated by Django 3.2.18 on 2024-04-12 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Amenities', '0006_alter_slotbooking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotbooking',
            name='description',
        ),
    ]
# Generated by Django 3.2.18 on 2024-04-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0002_booking_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='id_proof',
            field=models.FileField(null=True, upload_to='guest/static/guest_id'),
        ),
    ]

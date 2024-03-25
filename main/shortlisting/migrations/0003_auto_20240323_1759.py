# Generated by Django 3.2.18 on 2024-03-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlisting', '0002_rename_application_no_application_application_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoommateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_application_id', models.CharField(max_length=10)),
                ('receiver_application_id', models.CharField(max_length=10)),
                ('accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-17 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0005_auto_20201217_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_stock',
            name='profile_name',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-27 23:39

from django.db import migrations
from datetime import time
from assets.db import salons


def migrate_salons(apps, schema_editor):
    Salon = apps.get_model('beauty', 'Salon')
    
    for salon_data in salons:
        Salon.objects.create(
            name=salon_data['name'],
            address=salon_data['address'],
            working_time_from=time(9, 0),  # Устанавливаем время открытия 9:00
            working_time_to=time(21, 0)  # Устанавливаем время закрытия 21:00
        )


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_alter_profession_options_alter_salon_image'),
    ]

    operations = [
        migrations.RunPython(migrate_salons)
    ]

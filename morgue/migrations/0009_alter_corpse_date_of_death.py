# Generated by Django 4.0.6 on 2022-08-19 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morgue', '0008_typeofcorpse_room_no_of_shelves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpse',
            name='date_of_death',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 19, 14, 1, 55, 442917)),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-19 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morgue', '0006_care_taker_next_of_kin_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpse',
            name='date_of_death',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 7, 19, 22, 59, 8, 913225)),
        ),
        migrations.AlterField(
            model_name='corpse',
            name='time_of_admission',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

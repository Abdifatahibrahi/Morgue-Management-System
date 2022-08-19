# Generated by Django 4.0.6 on 2022-08-19 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morgue', '0009_alter_corpse_date_of_death'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeofcorpse',
            old_name='regular',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='typeofcorpse',
            name='vip',
        ),
        migrations.AlterField(
            model_name='corpse',
            name='date_of_death',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 19, 14, 2, 31, 376901)),
        ),
    ]

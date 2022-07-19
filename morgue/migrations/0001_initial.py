# Generated by Django 4.0.6 on 2022-07-19 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='corpse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Intersex', 'Intersex')], max_length=100)),
                ('Date_of_death', models.DateTimeField(auto_now=True)),
                ('Date_of_admission', models.DateTimeField(auto_now=True)),
                ('Time_of_admission', models.TimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.24 on 2021-08-06 21:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommedations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='DoctorLocationBased',
        ),
        migrations.DeleteModel(
            name='HospitalLocationBased',
        ),
    ]
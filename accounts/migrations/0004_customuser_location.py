# Generated by Django 2.2.24 on 2021-08-06 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommedations', '0002_auto_20210806_2125'),
        ('accounts', '0003_auto_20210806_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommedations.Location'),
        ),
    ]

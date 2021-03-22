# Generated by Django 2.2.12 on 2021-03-22 06:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_auto_20210322_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stghealthfacility',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True, validators=[django.core.validators.RegexValidator(message='Enter valid Latitude', regex='^[-+]?([1-8]?\\d(\\.\\d+)?|90(\\.0+)?)$'), django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)], verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='stghealthfacility',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=13, null=True, validators=[django.core.validators.RegexValidator(message='Enter valid Longitude', regex='^[-+]?(180(\\.0+)?|((1[0-7]\\d)|([1-9]?\\d))(\\.\\d+)?)$'), django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)], verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='stghealthfacility',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Please use correct phone number format', regex='^\\+?1?\\d{9,15}$')], verbose_name='Telephone'),
        ),
    ]
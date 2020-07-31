# Generated by Django 2.1.2 on 2020-07-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0006_auto_20200730_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stghealthfacility',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='stghealthfacility',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='stghealthfacility',
            name='url',
        ),
        migrations.AddField(
            model_name='stghealthfacilitytranslation',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stghealthfacilitytranslation',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stghealthfacilitytranslation',
            name='url',
            field=models.URLField(blank=True, max_length=2083, null=True, verbose_name='Web Address'),
        ),
    ]

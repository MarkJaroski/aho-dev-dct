# Generated by Django 2.1.2 on 2021-01-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_workforce', '0018_auto_20201205_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgannouncements',
            name='end_year',
            field=models.IntegerField(default=2021, verbose_name='Ending Period'),
        ),
        migrations.AlterField(
            model_name='stgannouncements',
            name='start_year',
            field=models.IntegerField(default=2021, verbose_name='Starting Period'),
        ),
        migrations.AlterField(
            model_name='stghealthworkforcefacts',
            name='end_year',
            field=models.IntegerField(default=2021, verbose_name='Ending Period'),
        ),
        migrations.AlterField(
            model_name='stghealthworkforcefacts',
            name='start_year',
            field=models.IntegerField(default=2021, verbose_name='Starting Period'),
        ),
        migrations.AlterField(
            model_name='stgrecurringevent',
            name='end_year',
            field=models.IntegerField(default=2021, verbose_name='Ending Period'),
        ),
        migrations.AlterField(
            model_name='stgrecurringevent',
            name='start_year',
            field=models.IntegerField(default=2021, verbose_name='Starting Period'),
        ),
    ]

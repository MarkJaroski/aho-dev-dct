# Generated by Django 2.2.12 on 2021-03-18 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0014_auto_20201024_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='StgLocationCodes',
            fields=[
                ('location', models.OneToOneField(help_text='You are not allowed to make changes to this Field because it             is related to countries already registed', on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='regions.StgLocation', verbose_name='Country')),
                ('country_code', models.CharField(max_length=15, unique=True, verbose_name='Phone Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Phone Code',
                'verbose_name_plural': 'Phone Codes',
                'db_table': 'stg_location_codes',
                'ordering': ('location',),
                'managed': True,
            },
        ),
    ]

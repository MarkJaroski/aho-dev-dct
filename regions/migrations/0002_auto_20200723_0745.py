# Generated by Django 2.1.2 on 2020-07-23 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stglocation',
            options={'managed': True, 'ordering': ['code'], 'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
    ]

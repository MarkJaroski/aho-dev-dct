# Generated by Django 2.1.2 on 2020-10-02 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0012_auto_20200914_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stglocation',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Location', 'verbose_name_plural': '   Locations'},
        ),
        migrations.AlterModelOptions(
            name='stglocationlevel',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Location Level', 'verbose_name_plural': '  Location Levels'},
        ),
    ]
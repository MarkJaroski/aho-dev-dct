# Generated by Django 2.1.2 on 2020-09-14 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0011_auto_20200914_1957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stgdataelement',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Element', 'verbose_name_plural': 'Data Elements'},
        ),
        migrations.AlterModelOptions(
            name='stgdataelementgroup',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Element Group', 'verbose_name_plural': ' Element Groups'},
        ),
    ]

# Generated by Django 2.1.2 on 2020-07-27 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20200727_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stgresourcetype',
            options={'managed': True, 'ordering': ('code',), 'verbose_name': 'Resource Type', 'verbose_name_plural': 'Resource Types'},
        ),
        migrations.AlterModelOptions(
            name='stgresourcetypetranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Resource Type Translation'},
        ),
    ]

# Generated by Django 2.1.2 on 2020-09-08 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0011_auto_20200906_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stgresourcetypetranslation',
            name='categorization',
        ),
    ]

# Generated by Django 2.1.2 on 2020-10-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0024_auto_20200919_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factdataindicator',
            options={'managed': True, 'ordering': ('indicator__name', 'location__name'), 'permissions': (('approve_factdataindicator', 'Can approve Indicator Data'), ('reject_factdataindicator', 'Can reject Indicator Data'), ('pend_factdataindicator', 'Can pend Indicator Data')), 'verbose_name': 'Indicator Data Record', 'verbose_name_plural': '    Single-record Form'},
        ),
        migrations.AlterModelOptions(
            name='stgindicator',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Indicator', 'verbose_name_plural': '  Indicators'},
        ),
        migrations.AlterModelOptions(
            name='stgindicatordomain',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Indicator Theme', 'verbose_name_plural': ' Indicator Themes'},
        ),
        migrations.AlterField(
            model_name='factdataindicator',
            name='string_value',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='String Value'),
        ),
    ]

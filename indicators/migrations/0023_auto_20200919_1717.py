# Generated by Django 2.1.2 on 2020-09-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0022_auto_20200914_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aho_factsindicator_archive',
            options={'managed': False, 'ordering': ('indicator__name', 'location__name'), 'verbose_name': 'Archive', 'verbose_name_plural': 'Indicators Archive'},
        ),
        migrations.AlterField(
            model_name='factdataindicator',
            name='string_value',
            field=models.CharField(blank=True, default='nul', max_length=500, null=True, verbose_name='String Value'),
        ),
        migrations.AlterField(
            model_name='factdataindicator',
            name='value_received',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Numeric Value'),
        ),
    ]
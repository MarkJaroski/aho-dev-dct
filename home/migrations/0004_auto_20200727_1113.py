# Generated by Django 2.1.2 on 2020-07-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200723_0936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stgmeasuremethod',
            options={'managed': True, 'verbose_name': ' Measure Type', 'verbose_name_plural': 'Indicator Measure Types'},
        ),
        migrations.AlterModelOptions(
            name='stgmeasuremethodtranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': ' Measure Type Translation'},
        ),
        migrations.AlterField(
            model_name='stgmeasuremethodtranslation',
            name='measure_value',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True, verbose_name='Measure Type'),
        ),
        migrations.AlterField(
            model_name='stgmeasuremethodtranslation',
            name='name',
            field=models.CharField(max_length=230, verbose_name='Name'),
        ),
    ]

# Generated by Django 2.1.2 on 2020-08-28 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200810_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgmeasuremethodtranslation',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='stgmeasuremethodtranslation',
            name='measure_value',
            field=models.DecimalField(blank=True, decimal_places=0, help_text='Ratio can be             factors like 1 for unit, 100, 1000,10000 or higher values', max_digits=50, null=True, verbose_name='Ratio'),
        ),
        migrations.AlterField(
            model_name='stgmeasuremethodtranslation',
            name='name',
            field=models.CharField(help_text='Name can be indicator types like unit,             Percentage, Per Thousand, Per Ten Thousand,Per Hundred Thousand etc', max_length=230, verbose_name='Measure Name'),
        ),
    ]

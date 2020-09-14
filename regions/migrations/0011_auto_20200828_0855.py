# Generated by Django 2.1.2 on 2020-08-28 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0010_auto_20200810_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stglocation',
            name='zone',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.PROTECT, to='regions.StgEconomicZones', verbose_name='Economic Block'),
        ),
    ]
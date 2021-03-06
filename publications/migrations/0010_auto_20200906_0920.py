# Generated by Django 2.1.2 on 2020-09-06 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0009_auto_20200905_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgknowledgeproduct',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Resource Location'),
        ),
        migrations.AlterField(
            model_name='stgproductdomain',
            name='publications',
            field=models.ManyToManyField(blank=True, db_table='stg_product_domain_members', to='publications.StgKnowledgeProduct', verbose_name='Resources'),
        ),
    ]

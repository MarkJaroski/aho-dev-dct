# Generated by Django 2.1.2 on 2020-10-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0015_auto_20201015_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgresourcecategorytranslation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='stgresourcecategorytranslation',
            name='name',
            field=models.CharField(max_length=230, verbose_name='Category Name'),
        ),
    ]

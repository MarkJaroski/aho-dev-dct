# Generated by Django 2.1.2 on 2021-01-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0016_auto_20201024_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgknowledgeproducttranslation',
            name='year_published',
            field=models.IntegerField(default=2021, verbose_name='Year Published'),
        ),
    ]

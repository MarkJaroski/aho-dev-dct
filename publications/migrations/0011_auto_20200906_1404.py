# Generated by Django 2.1.2 on 2020-09-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_auto_20200906_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgproductdomaintranslation',
            name='level',
            field=models.SmallIntegerField(choices=[(1, 'level 1'), (2, 'level 2'), (3, 'level 3'), (4, 'level 4'), (5, 'level 5'), (6, 'level 6')], default=1, verbose_name='Theme Level'),
        ),
    ]

# Generated by Django 2.2.12 on 2021-03-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0019_remove_stgknowledgeproduct_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgknowledgeproducttranslation',
            name='title',
            field=models.CharField(max_length=2000, verbose_name='Title'),
        ),
    ]
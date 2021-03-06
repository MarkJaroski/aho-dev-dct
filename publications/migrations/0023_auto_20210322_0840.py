# Generated by Django 2.2.12 on 2021-03-22 05:40

import django.core.validators
from django.db import migrations, models
import publications.models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0022_stgknowledgeproduct_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgknowledgeproducttranslation',
            name='year_published',
            field=models.PositiveIntegerField(default=2021, help_text='This marks year of publication', validators=[django.core.validators.MinValueValidator(1900), publications.models.max_value_current_year], verbose_name='Year Published'),
        ),
    ]

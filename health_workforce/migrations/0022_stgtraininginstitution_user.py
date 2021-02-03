# Generated by Django 2.1.2 on 2021-02-03 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health_workforce', '0021_stghealthworkforcefacts_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='stgtraininginstitution',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Name (Email)'),
        ),
    ]

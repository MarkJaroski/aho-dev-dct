# Generated by Django 2.1.2 on 2021-02-03 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0018_stgknowledgeproduct_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stgknowledgeproduct',
            name='user',
        ),
    ]

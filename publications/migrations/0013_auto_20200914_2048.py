# Generated by Django 2.1.2 on 2020-09-14 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0012_remove_stgresourcetypetranslation_categorization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stgknowledgeproduct',
            options={'managed': True, 'ordering': ('translations__title',), 'permissions': (('approve_stgknowledgeproduct', 'Can approve stgknowledgeproduct'), ('reject_stgknowledgeproduct', 'Can reject stgknowledgeproduct'), ('pend_stgknowledgeproduct', 'Can pend stgknowledgeproduct')), 'verbose_name': 'Knowledge Resource', 'verbose_name_plural': 'Knowledge Resources'},
        ),
        migrations.AlterModelOptions(
            name='stgproductdomain',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Resource Theme', 'verbose_name_plural': 'Resource Themes'},
        ),
        migrations.AlterModelOptions(
            name='stgresourcecategory',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Resource Category', 'verbose_name_plural': 'Resource Categories'},
        ),
        migrations.AlterModelOptions(
            name='stgresourcetype',
            options={'managed': True, 'ordering': ('translations__name',), 'verbose_name': 'Resource Type', 'verbose_name_plural': 'Resource Types'},
        ),
    ]
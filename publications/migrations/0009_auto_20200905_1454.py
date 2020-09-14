# Generated by Django 2.1.2 on 2020-09-05 11:54

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0008_auto_20200810_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='StgResourceCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Resource Category',
                'verbose_name_plural': 'Resource Categories',
                'db_table': 'stg_resource_category',
                'ordering': ('code',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgResourceCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='category Name')),
                ('shortname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='publications.StgResourceCategory')),
            ],
            options={
                'verbose_name': 'Resource Category Translation',
                'db_table': 'stg_resource_category_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='stgknowledgeproducttranslation',
            name='categorization',
        ),
        migrations.AddField(
            model_name='stgresourcetypetranslation',
            name='shortname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Name'),
        ),
        migrations.AddField(
            model_name='stgknowledgeproduct',
            name='categorization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='publications.StgResourceCategory', verbose_name='Resource Category'),
        ),
        migrations.AlterUniqueTogether(
            name='stgresourcecategorytranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
# Generated by Django 2.1.2 on 2020-08-18 15:39

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0010_auto_20200810_1940'),
        ('health_workforce', '0012_auto_20200818_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='StgAnnouncements',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=45, unique=True, verbose_name='Code')),
                ('internal_url', models.FileField(blank=True, upload_to='media/files/events', verbose_name='Upload File/Video(s)')),
                ('external_url', models.CharField(blank=True, max_length=2083, null=True, verbose_name='Web Link (URL)')),
                ('cover_image', models.ImageField(blank=True, upload_to='media/images/events', verbose_name='Upload Picture/Banner(s)')),
                ('start_year', models.IntegerField(default=2020, verbose_name='Starting Period')),
                ('end_year', models.IntegerField(default=2020, verbose_name='Ending Period')),
                ('period', models.CharField(blank=True, max_length=10, verbose_name='Period')),
                ('status', models.CharField(choices=[('active', 'Open'), ('inactive', 'Closed'), ('suspended', 'Suspended')], default='active', max_length=10, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
                'db_table': 'stg_event_announcement',
                'ordering': ('event_id',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgAnnouncementsTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Announcment Title')),
                ('shortname', models.CharField(max_length=230, verbose_name='Short Title')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Event Message')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgAnnouncements')),
            ],
            options={
                'verbose_name': 'Announcement Translation',
                'db_table': 'stg_event_announcement_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='stgrecurringevent',
            unique_together={('location', 'start_year', 'end_year')},
        ),
        migrations.AlterUniqueTogether(
            name='stgannouncementstranslation',
            unique_together={('language_code', 'master')},
        ),
        migrations.AlterUniqueTogether(
            name='stgannouncements',
            unique_together={('location', 'start_year', 'end_year')},
        ),
    ]

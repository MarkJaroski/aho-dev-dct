# Generated by Django 2.2.12 on 2021-03-18 11:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import health_workforce.models
import parler.fields
import parler.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publications', '0020_auto_20210315_1356'),
        ('home', '0020_auto_20201205_1938'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regions', '0015_stglocationcodes'),
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
                ('start_year', models.PositiveIntegerField(default=2021, help_text='This marks the start of reporting period', validators=[django.core.validators.MinValueValidator(1900), health_workforce.models.max_value_current_year], verbose_name='Starting period')),
                ('end_year', models.PositiveIntegerField(default=2021, help_text='This marks the end of reporting. The value must be current             year or greater than the start year', validators=[django.core.validators.MinValueValidator(1900), health_workforce.models.max_value_current_year], verbose_name='Ending Period')),
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
                'ordering': ('translations__name',),
                'managed': True,
                'unique_together': {('location', 'start_year', 'end_year')},
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgHealthCadre',
            fields=[
                ('cadre_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=45, unique=True, verbose_name='ISCO-08 Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('parent', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='health_workforce.StgHealthCadre', verbose_name='Parent Cadre')),
            ],
            options={
                'verbose_name': 'Health Cadre',
                'verbose_name_plural': '   Health Cadres',
                'db_table': 'stg_health_cadre',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgInstitutionProgrammes',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Training Programme',
                'verbose_name_plural': ' Training Programmes',
                'db_table': 'stg_institution_programme',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgInstitutionType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Institution Type',
                'verbose_name_plural': ' Institution Types',
                'db_table': 'stg_institution_type',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgRecurringEvent',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=45, unique=True, verbose_name='Event Code')),
                ('internal_url', models.FileField(blank=True, upload_to='media/files/events', verbose_name='Upload File/Video(s)')),
                ('external_url', models.CharField(blank=True, max_length=2083, null=True, verbose_name='Web Address (URL)')),
                ('cover_image', models.ImageField(blank=True, upload_to='media/images/events', verbose_name='Upload Picture/Banner(s)')),
                ('start_year', models.PositiveIntegerField(default=2021, help_text='This marks the start of reporting period', validators=[django.core.validators.MinValueValidator(1900), health_workforce.models.max_value_current_year], verbose_name='Starting period')),
                ('end_year', models.PositiveIntegerField(default=2021, help_text='This marks the end of reporting. The value must be current             year or greater than the start year', validators=[django.core.validators.MinValueValidator(1900), health_workforce.models.max_value_current_year], verbose_name='Ending Period')),
                ('period', models.CharField(blank=True, max_length=10, verbose_name='Period')),
                ('status', models.CharField(choices=[('active', 'Open'), ('inactive', 'Closed'), ('suspended', 'Suspended')], default='active', max_length=10, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('cadre_id', models.ManyToManyField(blank=True, db_table='stg_recurring_event_lookup', to='health_workforce.StgHealthCadre', verbose_name='Target Focus')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Event Location')),
            ],
            options={
                'verbose_name': 'Nursing & Midwifery',
                'verbose_name_plural': 'Nursing and Midwifery',
                'db_table': 'stg_recurring_event',
                'ordering': ('translations__name',),
                'managed': True,
                'unique_together': {('location', 'start_year', 'end_year')},
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgTrainingInstitution',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=15, unique=True, verbose_name='Institution Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('location', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Location')),
                ('programmes', models.ManyToManyField(blank=True, db_table='stg_institution_programs_lookup', to='health_workforce.StgInstitutionProgrammes', verbose_name='Training Programmes')),
                ('type', models.ForeignKey(default=6, on_delete=django.db.models.deletion.PROTECT, to='health_workforce.StgInstitutionType', verbose_name='Institution Type')),
                ('user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Name (Email)')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': '  Training Institutions',
                'db_table': 'stg_traininginstitution',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HumanWorkforceResourceProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Resource/Guide',
                'verbose_name_plural': 'Resources/Guides',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('publications.stgknowledgeproduct',),
        ),
        migrations.CreateModel(
            name='ResourceCategoryProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Resource Category',
                'verbose_name_plural': 'Resource Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('publications.stgresourcecategory',),
        ),
        migrations.CreateModel(
            name='ResourceTypeProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Resource Type',
                'verbose_name_plural': 'Resource Types',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('publications.stgresourcetype',),
        ),
        migrations.CreateModel(
            name='StgHealthWorkforceFacts',
            fields=[
                ('fact_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Data Value')),
                ('start_year', models.PositiveIntegerField(default=2021, help_text='This marks the start of reporting period', validators=[django.core.validators.MinValueValidator(1900), health_workforce.models.max_value_current_year], verbose_name='Starting period')),
                ('end_year', models.PositiveIntegerField(default=2021, help_text='This marks the end of reporting. The value must be current             year or greater than the start year', validators=[django.core.validators.MinValueValidator(1900), health_workforce.models.max_value_current_year], verbose_name='Ending Period')),
                ('period', models.CharField(blank=True, max_length=10, verbose_name='Period')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('cadre_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='health_workforce.StgHealthCadre', verbose_name='Occupation/Cadre')),
                ('categoryoption', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.StgCategoryoption', verbose_name='Disaggregation Options')),
                ('datasource', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.StgDatasource', verbose_name='Data Source')),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Location')),
                ('measuremethod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.StgMeasuremethod', verbose_name='Measure Type')),
                ('user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Name (Email)')),
            ],
            options={
                'verbose_name': 'Health Workforce',
                'verbose_name_plural': '    Health Workforce',
                'db_table': 'fact_health_workforce',
                'ordering': ('cadre_id',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StgTrainingInstitutionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Institution Name')),
                ('faculty', models.CharField(blank=True, max_length=150, null=True, verbose_name='Faculty Name')),
                ('accreditation', models.CharField(choices=[('accredited', 'Accredited'), ('charterted', 'Chartered'), ('unacredited', 'Not Accredited'), ('pending', 'Pending Accreditation')], default='accredited', max_length=50, verbose_name='Accreditation Status')),
                ('regulator', models.CharField(blank=True, max_length=150, null=True, verbose_name='Regulatory Body')),
                ('accreditation_info', models.CharField(blank=True, max_length=2000, verbose_name='Accreditation Details')),
                ('language', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teaching Language')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Contact Person')),
                ('posta', models.CharField(blank=True, max_length=500, null=True, verbose_name='Post Address')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone format: '+999999999' maximum 15.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('url', models.URLField(blank=True, max_length=2083, null=True, verbose_name='Web Address')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgTrainingInstitution')),
            ],
            options={
                'verbose_name': 'Institution Translation',
                'db_table': 'stg_traininginstitution_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgRecurringEventTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(default='International Year of the Nurse and the Midwife', max_length=230, verbose_name='Name of Event')),
                ('shortname', models.CharField(max_length=230, verbose_name='Short Name')),
                ('theme', models.TextField(blank=True, null=True, verbose_name='Theme')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgRecurringEvent')),
            ],
            options={
                'verbose_name': 'Nursing & Midwifery Translation',
                'db_table': 'stg_recurring_event_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgInstitutionTypeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Name')),
                ('shortname', models.CharField(blank=True, max_length=230, null=True, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgInstitutionType')),
            ],
            options={
                'verbose_name': 'Institution Type Translation',
                'db_table': 'stg_institution_type_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgInstitutionProgrammesTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Type Name')),
                ('shortname', models.CharField(blank=True, max_length=230, null=True, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgInstitutionProgrammes')),
            ],
            options={
                'verbose_name': 'Training Programme Translation',
                'db_table': 'stg_institution_programme_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgHealthCadreTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Cadre Name')),
                ('shortname', models.CharField(max_length=230, verbose_name='Short Name')),
                ('academic', models.CharField(choices=[('degree', 'Degree'), ('diploma', 'Diploma'), ('masters', 'Masters'), ('phd', 'Doctorate'), ('certificate', 'Certificate'), ('basic', 'Basic Education')], default='degree', max_length=10, verbose_name='Academic Qualification')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgHealthCadre')),
            ],
            options={
                'verbose_name': 'Health Cadre Translation',
                'db_table': 'stg_health_cadre_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgAnnouncementsTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Announcment Title')),
                ('shortname', models.CharField(max_length=230, verbose_name='Short Title')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='health_workforce.StgAnnouncements')),
            ],
            options={
                'verbose_name': 'Announcement Translation',
                'db_table': 'stg_event_announcement_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]

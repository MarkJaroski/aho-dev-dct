from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields import DecimalField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from home.models import (StgDatasource,StgCategoryoption,StgMeasuremethod,
    StgValueDatatype)
from regions.models import StgLocation

def make_choices(values):
    return [(v, v) for v in values]

STATUS_CHOICES = ( #choices for approval of indicator data by authorized users
    ('pending', 'Pending'),
    ('approved','Approved'),
    ('rejected','Rejected'),
)

class StgIndicatorReference(TranslatableModel):
    reference_id = models.AutoField(primary_key=True)  # Field name made lowercase
    uuid = uuid = models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    translations = TranslatedFields(
        name = models.CharField(_("Reference Name"),max_length=230, blank=False,
            null=False,default=_("Global List of 100 Core Health Indicators")),
        shortname = models.CharField(_('Short Name'),max_length=50,
            blank=True, null=True),
        description = models.TextField(_('Brief Description'),blank=True, null=True)
    )
    code = models.CharField(unique=True, max_length=50, blank=True,null=True)
    date_created = models.DateTimeField(_('Date Created'),blank=True,null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True,auto_now=True)

    class Meta:
        managed = True
        db_table = 'stg_indicator_reference'
        verbose_name = _('Indicator Reference')
        verbose_name_plural = _('Indicator References')
        ordering = ('code', )

    def __str__(self):
        return self.name #display the data source name

    # The filter function need to be modified to work with django parler as follows:
    def clean(self): # Don't allow end_period to be greater than the start_period.
        if StgIndicatorReference.objects.filter(
            translations__name=self.name).count() and not self.reference_id:
            raise ValidationError({'name':_('Sorry! This indicator reference exists')})

    def save(self, *args, **kwargs):
        super(StgIndicatorReference, self).save(*args, **kwargs)

class StgIndicator(TranslatableModel):
    indicator_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    uuid =models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    translations = TranslatedFields(any_language=True,
        name = models.CharField(_('Indicator Name'),max_length=500,
            blank=False, null=False),  # Field name made lowercase.
        shortname = models.CharField(_('Short Name'),unique=True, max_length=120,
            blank=False,null=True),  # Field name made lowercase.
        definition = models.TextField(_('Indicator Definition'),blank=False,
            null=True,),  # Field name made lowercase.
        preferred_datasources = models.CharField(_('Primary Sources'),
            max_length=5000,blank=True, null=True,),  # Field name made lowercase.
        numerator_description = models.TextField(_('Numerator Description'),
            blank=True,null=True,),  # Field name made lowercase.
        denominator_description = models.TextField(_('Denominator Description'),
            blank=True,null=True)
    )
    afrocode = models.CharField(_('Regional Code'),max_length=10,blank=True,
        null=False,unique=True)  # Field name made lowercase.
    gen_code = models.CharField(_('Global Code'),max_length=10, blank=True,
        null=True,)  # Field name made lowercase.
    reference = models.ForeignKey(StgIndicatorReference, models.PROTECT,
        default=1, verbose_name =_('Indicator Reference'))  # Field name made lowercase.
    date_created = models.DateTimeField(_('Date Created'),blank=True, null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'stg_indicator'
        verbose_name = _('Indicator')
        verbose_name_plural = _('Indicators')

    # This method makes it possible to enter multi-records in the Tabular form
    # without returning the language code error! resolved on 10th August 2020
    def __str__(self):
        return self.safe_translation_getter(
            'name', any_language=True,language_code=settings.LANGUAGE_CODE)

    # The filter function need to be modified to work with django parler as follows:
    def clean(self): # Don't allow end_period to be greater than the start_period.
        if StgIndicator.objects.filter(
            translations__name=self.name).count() and not self.indicator_id:
            raise ValidationError({'name':_('Sorry! Indicator with this name exists')})

    def save(self, *args, **kwargs):
        super(StgIndicator, self).save(*args, **kwargs)


class StgIndicatorDomain(TranslatableModel):
    LEVEL = (
    (1, 'level 1'),
    (2, 'level 2'),
    (3,'level 3'),
    (4,'level 4'),
    (5,'level 5'),
    (6,'level 6'),
    )

    domain_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    uuid = uuid = models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    translations = TranslatedFields(
        name = models.CharField(_('Theme'),max_length=150, blank=False,
        null=False),
        shortname = models.CharField(_('Short Name'),max_length=45,blank=False,
            null=False),

        description = models.TextField(_('Brief Description'),blank=True, null=True,)
    )
    level =models.SmallIntegerField(_('Theme Level'),choices=LEVEL,
        default=LEVEL[0][0])
    code = models.CharField(unique=True, max_length=45, blank=True,
        null=True, verbose_name = _('Code'))
    parent = models.ForeignKey('self', models.PROTECT, blank=True, null=True,
        verbose_name = _('Parent Theme'))  # Field name made lowercase.
    # this field establishes a many-to-many relationship with the domain table
    indicators = models.ManyToManyField(StgIndicator,
        db_table='stg_indicator_domain_members',blank=True,
        verbose_name = _('Indicators'))  # Field name made lowercase.
    date_created = models.DateTimeField(_('Date Created'),blank=True, null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'stg_indicator_domain'
        verbose_name = _('Indicator Theme')
        verbose_name_plural = _('Indicator Themes')
        ordering = ('code', )

    def __str__(self):
        return self.name #ddisplay disagregation options

    # The filter function need to be modified to work with django parler as follows:
    def clean(self): # Don't allow end_period to be greater than the start_period.
        if StgIndicatorDomain.objects.filter(
            translations__name=self.name).count() and not self.domain_id:
            raise ValidationError({'name':_('Sorry! This indicators theme exists')})

    def save(self, *args, **kwargs):
        super(StgIndicatorDomain, self).save(*args, **kwargs)


class FactDataIndicator(models.Model):
  # discriminator for ownership of data this was decided on 13/12/2019 with Gift
    fact_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    uuid = uuid = models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    indicator = models.ForeignKey(StgIndicator, models.PROTECT,
        verbose_name = _('Indicator Name'))  # Field name made lowercase.
    location = models.ForeignKey(StgLocation, models.PROTECT,
        verbose_name = _('Location Name'))  # Field name made lowercase.
    categoryoption = models.ForeignKey(StgCategoryoption, models.PROTECT,blank=False,
        verbose_name =_('Disaggregation Options'), default=999)  # Field name made lowercase.
    # This field is used to lookup sources of data such as routine systems, census and surveys
    datasource = models.ForeignKey(StgDatasource, models.PROTECT,
        verbose_name = _('Data Source'))  # Field name made lowercase.
    # This field is used to lookup the type of data required such as text, integer or float
    measuremethod = models.ForeignKey(StgMeasuremethod, models.PROTECT,blank=True,
        null=True, verbose_name =_('Measure Type'))  # Field name made lowercase.
    numerator_value = models.DecimalField(_('Numerator Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)
    denominator_value = models.DecimalField(_('Denominator Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    value_received = DecimalField(_('Data Value'),max_digits=20,decimal_places=2,
        blank=True)  # Field name made lowercase.
    min_value = models.DecimalField(_('Minimum Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    max_value = models.DecimalField(_('Maximum Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    target_value = models.DecimalField(_('Target Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    start_period = models.IntegerField(_('Starting period'),null=False,blank=False,
        default=datetime.date.today().year,#extract current date year value only
        help_text=_("This marks the start of reporting period"))
    end_period  = models.IntegerField(_('Ending Period'),null=False,blank=False,
        default=datetime.date.today().year, #extract current date year value only
        help_text=_("This marks the end of reporting. The value must be current \
            year or greater than the start year"))
    period = models.CharField(_('Period'),max_length=25,blank=True,null=False) #try to concatenate period field
    comment = models.CharField(_('Status'),max_length=10, choices= STATUS_CHOICES,
        default=STATUS_CHOICES[0][0])  # Field name made lowercase.
    string_value= models.CharField(_('Comments'),max_length=500,blank=True,null=True) # davy's request as of 30/4/2019
    date_created = models.DateTimeField(_('Date Created'),blank=True, null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True, auto_now=True)

    class Meta:
        permissions = (
            ("approve_factdataindicator","Can approve Indicator Data"),
            ("reject_factdataindicator","Can reject Indicator Data"),
            ("pend_factdataindicator","Can pend Indicator Data")
        )

        managed = True
        db_table = 'fact_data_indicator'
        verbose_name = _('Indicator Record')
        verbose_name_plural = _('Single-record Form')
        ordering = ('location__name',)
        unique_together = ('indicator', 'location', 'categoryoption','datasource',
            'start_period','end_period') #enforces concatenated unique constraint

    def __str__(self):
         return str(self.indicator)

    """
    The purpose of this method is to compare the start_period to the end_period. If the
    start_period is greater than the end_period athe model should show an inlines error
    message and wait until the user corrects the mistake.
    """
    def clean(self): # Don't allow end_period to be greater than the start_period.
        if self.start_period <=1990 or self.start_period > datetime.date.today().year:
            raise ValidationError({'start_period':_(
                'Sorry! Start year cannot be less than 1990 or greater than current Year ')})
        elif self.end_period <=1990 or self.end_period > datetime.date.today().year:
            raise ValidationError({'end_period':_(
                'Sorry! The ending year cannot be lower than the start year or \
                greater than the current Year ')})
        elif self.end_period < self.start_period and self.start_period is not None:
            raise ValidationError({'end_period':_(
                'Sorry! Ending period cannot be lower than the start period. \
                 Please make corrections')})

        #This logic ensures that a maximum value is provided for a corresponing minimum value
        if self.min_value is not None and self.min_value !='':
            if self.max_value is None or self.max_value < self.min_value:
                raise ValidationError({'max_value':_(
                    'Data Integrity Problem! You must provide a Maximum that is \
                     greater that Minimum value ')})
            elif self.value_received is not None and self.value_received <= self.min_value:
                raise ValidationError({'min_value':_(
                    'Data Integrity Problem! Minimum value cannot be greater \
                     that the nominal value')})


    """
    The purpose of this method is to concatenate the date that are entered as
    start_period and end_period and save the concatenated value as a string in
    the database ---this is very important to take care of Davy's date complexity
    """
    def get_period(self):
        if self.period is None or (self.start_period and self.end_period):
            if self.start_period == self.end_period:
                period = int(self.start_period)
            else:
                period =str(int(self.start_period))+"-"+ str(int(self.end_period))
        return period

    """
    This method overrides the save method to store the derived field into database.
    Note that the last line calls the super class FactDataIndicator to save the value
    """
    def save(self, *args, **kwargs):
        self.period = self.get_period()
        super(FactDataIndicator, self).save(*args, **kwargs)

# These proxy classes are used to register menu in the admin for tabular entry
class IndicatorProxy(StgIndicator):
    """
    Creates permissions for proxy models which are not created automatically by
    'django.contrib.auth.management.create_permissions'.Since we can't rely on
    'get_for_model' we must fallback to  'get_by_natural_key'. However, this
    method doesn't automatically create missing 'ContentType' so we must ensure
    all the models' 'ContentType's are created before running this method.
    We do so by unregistering the 'update_contenttypes' 'post_migrate' signal
    and calling it in here just before doing everything.
    """
    def create_proxy_permissions(app, created_models, verbosity, **kwargs):
        update_contenttypes(app, created_models, verbosity, **kwargs)
        app_models = models.get_models(app)
        # The permissions we're looking for as (content_type, (codename, name))
        searched_perms = list()
        # The codenames and ctypes that should exist.
        ctypes = set()
        for model in app_models:
            opts = model._meta
            if opts.proxy:
                # Can't use 'get_for_model' here since it doesn't return correct 'ContentType' for proxy models
                # See https://code.djangoproject.com/ticket/17648
                app_label, model = opts.app_label, opts.object_name.lower()
                ctype = ContentType.objects.get_by_natural_key(app_label, model)
                ctypes.add(ctype)
                for perm in _get_all_permissions(opts, ctype):
                    searched_perms.append((ctype, perm))

        # Find all the Permissions that have a content_type for a model we're looking for.
        #We don't need to check for codenames since we already have a list of the ones we're going to create.
        all_perms = set(Permission.objects.filter(
            content_type__in=ctypes,
        ).values_list(
            "content_type", "codename"
        ))

        objs = [
            Permission(codename=codename, name=name, content_type=ctype)
            for ctype, (codename, name) in searched_perms
            if (ctype.pk, codename) not in all_perms
        ]
        Permission.objects.bulk_create(objs)
        if verbosity >= 2:
            for obj in objs:
                sys.stdout.write("Adding permission '%s'" % obj)
        models.signals.post_migrate.connect(create_proxy_permissions)
        models.signals.post_migrate.disconnect(update_contenttypes)

    class Meta:
        managed = False
        verbose_name = 'Data Grid Form'
        verbose_name_plural = '   Multi-records Grid'
        proxy = True

    """
    This def clean (self) method was contributed by Daniel Mbugua to resolve
    the issue of parent-child saving issue in the multi-records entry form.
    My credits to Mr Mbugua of MSc DCT, UoN-Kenya
    """
    def clean(self): #Appreciation to Daniel M.
        pass


#This model class maps to a database view that looks up the django_admin logs, location, customuser and group
class AhoDoamain_Lookup(models.Model):
    indicator_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    indicator_name = models.CharField(_("Indicator Name"),blank=False,null=False,
        max_length=500)
    code = models.CharField(_("Indicator Code"),max_length=10, blank=True)
    domain_name  = models.CharField(_("Theme"),max_length=230, blank=True)
    domain_level  = models.IntegerField(_("Theme Level"),null=False,blank=False)

    class Meta:
        managed = False
        db_table = 'aho_domain_lookup'
        verbose_name = _('Theme Lookup')
        verbose_name_plural = _('Themes Lookup')
        ordering = ('indicator_name', )

    def __str__(self):
        return self.indicator_name


class aho_factsindicator_archive(models.Model):
    fact_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    uuid =models.CharField(_('Unique ID'),unique=True,max_length=36, blank=False,
        null=False,default=uuid.uuid4,editable=False)
    indicator = models.ForeignKey('StgIndicator', models.PROTECT,blank=False,
        null=False, verbose_name = _('Indicator Name'))  # Field name made lowercase.
    location = models.ForeignKey(StgLocation, models.PROTECT,
        verbose_name = _('Location Name'))
    categoryoption = models.ForeignKey(StgCategoryoption, models.PROTECT,blank=False,
        verbose_name = _('Disaggregation Option'), default=99)  # Field name made lowercase.
    datasource = models.ForeignKey(StgDatasource, models.PROTECT,blank=False,
        null=False, verbose_name = _('Data Source'))  # Field name made lowercase.
    measuremethod = models.ForeignKey(StgMeasuremethod, models.PROTECT,blank=True,
        null=True, verbose_name = _('Measure Type'))  # Field name made lowercase.
    value_received = models.DecimalField(_('Value'),max_digits=20,decimal_places=2,
        blank=False,null=True)  # Field name made lowercase.
    numerator_value = models.DecimalField(_('Numerator Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    denominator_value = models.DecimalField(_('Denominator Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    min_value = models.DecimalField(_('Minimum Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    max_value = models.DecimalField(_('Maximum Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    target_value = models.DecimalField(_('Target Value'),max_digits=20,
        decimal_places=2,blank=True, null=True)  # Field name made lowercase.
    start_period = models.IntegerField(_('Starting Period',),null=False,
        blank=False,default=datetime.date.today().year,#extract current date year value only
        help_text=_("This Year marks the start of the reporting period. \
            NB: 1990 is the Lowest Limit!"))
    end_period  = models.IntegerField(_('Ending Year'),null=False,blank=False,
        default=datetime.date.today().year, #extract current date year value only
        help_text=_("This Year marks the end of reporting. \
        The value must be current year or greater than the start year"))
    period = models.CharField(_('Period'),max_length=25,blank=True,null=False) #try to concatenate period field
    comment = models.CharField(_('Status'),max_length=10,choices= STATUS_CHOICES,
        default=STATUS_CHOICES[0][0])
    string_value=models.CharField(_('Comments'),max_length=500,blank=True,
        null=True) # davy's request as of 30/4/2019

    class Meta:
        managed = False
        db_table = 'aho_factsindicator_archive'
        verbose_name = _('Archive')
        verbose_name_plural = _('Indicators Archive')
        ordering = ('location__name',)

    def __str__(self):
         return str(self.indicator)


class StgNarrative_Type(TranslatableModel):
    type_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    uuid = uuid = models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    code = models.CharField(unique=True, max_length=50, blank=True, null=False,
        verbose_name = 'Code')  # Field name made lowercase.
    translations = TranslatedFields(
        name = models.CharField(_('Name'),max_length=500, blank=False, null=False),  # Field name made lowercase.
        shortname = models.CharField(_('Short Name'),unique=True, max_length=120,
            blank=False,null=True),  # Field name made lowercase.
        description = models.TextField(_('Brief Description'),blank=False,null=True)
    )
    date_created = models.DateTimeField(_('Date Created'),blank=True, null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'stg_narrative_type'
        verbose_name = _('Narrative Type')
        verbose_name_plural = _('Narrative Types')
        ordering = ('code',)

    def __str__(self):
        return self.name #display the knowledge product category name


    # The filter function need to be modified to work with django parler as follows:
    def clean(self): # Don't allow end_period to be greater than the start_period.
        if StgNarrative_Type.objects.filter(
            translations__name=self.name).count() and not self.type_id:
            raise ValidationError({'name':_('Sorry! This narrative type exists')})

    def save(self, *args, **kwargs):
        super(StgNarrative_Type, self).save(*args, **kwargs)


class StgAnalyticsNarrative(models.Model):
    analyticstext_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    narrative_type = models.ForeignKey(StgNarrative_Type,models.PROTECT,
        verbose_name = _('Narrative Type'))
    domain = models.ForeignKey(StgIndicatorDomain,models.PROTECT,  blank=False,
        null=False,verbose_name = _('Theme'),  default = 1)
    location = models.ForeignKey(StgLocation, models.PROTECT, blank=False,
        null=False,verbose_name = _('Location'), default = 1)
    code = models.CharField(unique=True, max_length=50, blank=True, null=False,
        verbose_name = 'Code')  # Field name made lowercase.
    narrative_text = models.TextField(_('Narrative Text'),blank=False, null=False)  # Field name made lowercase.
    date_created = models.DateTimeField(_('Date Created'),blank=True, null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True, auto_now=True)

    class Meta:
        managed = True
        db_table = 'stg_analytics_narrative'
        verbose_name = _('Theme Narrative')
        verbose_name_plural = _('Theme Narratives')
        ordering = ('-narrative_type',) #sorted in descending order by date created

    def __str__(self):
        return self.narrative_text


class StgIndicatorNarrative(models.Model):
    indicatornarrative_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(_('Unique ID'),unique=True,max_length=36,
        blank=False, null=False,default=uuid.uuid4,editable=False)
    narrative_type = models.ForeignKey(StgNarrative_Type,models.PROTECT,
        verbose_name = _('Narrative Type'))
    indicator = models.ForeignKey('StgIndicator', models.PROTECT,blank=False,
        null=False,verbose_name = _('Indicator'))
    location = models.ForeignKey(StgLocation, models.PROTECT, blank=False, null=False,
         verbose_name = _('Location'), default = 1)
    code = models.CharField(unique=True, max_length=50, blank=True, null=False,
        verbose_name = 'Code')  # Field name made lowercase.
    narrative_text = models.TextField(_('Narrative Text'),blank=False, null=False)  # Field name made lowercase.
    date_created = models.DateTimeField(_('Date Created'),blank=True, null=True,
        auto_now_add=True)
    date_lastupdated = models.DateTimeField(_('Date Modified'),blank=True,
        null=True, auto_now=True)

    class Meta:
         managed = True
         db_table = 'stg_indicator_narrative'
         verbose_name = _('Indicator Narrative')
         verbose_name_plural = _('Indicators Narrative')
         ordering = ('-narrative_type',)

    def __str__(self):
         return str(self.indicator)

from django.db import models
import uuid
from datetime import datetime #for handling year part of date filed
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _ # The _ is alias for gettext
from parler.models import TranslatableModel,TranslatedFields
from regions.models import StgLocation

def make_choices(values):
    return [(v, v) for v in values]

# New model to take care of resource types added 11/05/2019 courtesy of Gift
class StgFacilityType(TranslatableModel):
    type_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, max_length=50, blank=True,
        null=True, verbose_name = 'Facility Code')  # Field name made lowercase.
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Facility Type'),  # Field name made lowercase.
        shortname = models.CharField(unique=True,max_length=50,blank=False,null=False,
            verbose_name = 'Short Name'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description')  # Field name made lowercase.
    )
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_facility_type'
        verbose_name = 'Facility Type'
        verbose_name_plural = 'Facility Types'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the knowledge product category name

    def clean(self):
        if StgFacilityType.objects.filter(
            translations__name=self.name).count() and not self.type_id and not \
                self.code:
            raise ValidationError({'name':_('Facility type with the same \
                name exists')})

    def save(self, *args, **kwargs):
        super(StgFacilityType, self).save(*args, **kwargs)


# New model to take care of resource types added 11/05/2019 courtesy of Gift
class StgFacilityInfrastructure(TranslatableModel):
    infra_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, max_length=50, blank=True,
        null=True, verbose_name = 'Infrastructure Code')  # Field name made lowercase.
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Infrastructure Name'),  # Field name made lowercase.
        shortname = models.CharField(unique=True,max_length=50,blank=False,null=False,
            verbose_name = 'Short Name'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description')  # Field name made lowercase.
    )
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_facility_infrastructure'
        verbose_name = 'Infratsrucrure'
        verbose_name_plural = 'Infrastructures'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the knowledge product category name

    def clean(self):
        if StgFacilityInfrastructure.objects.filter(
            translations__name=self.name).count() and not self.infra_id and not \
                self.code:
            raise ValidationError({'name':_('Resource type with the same \
                name exists')})

    def save(self, *args, **kwargs):
        super(StgFacilityInfrastructure, self).save(*args, **kwargs)


class StgFacilityOwnership(TranslatableModel):
    owner_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, max_length=50, blank=True,
        null=True, verbose_name = 'Ownership Code')  # Field name made lowercase.
    location = models.ForeignKey(StgLocation, models.PROTECT,
        verbose_name = 'Location Name')  # Field name made lowercase.
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Facility Owner'),
        shortname = models.CharField(unique=True,max_length=50,blank=False,null=False,
            verbose_name = 'Short Name'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description')  # Field name made lowercase.
    )
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_facility_owner'
        verbose_name = 'Ownership'
        verbose_name_plural = 'Facility Owners'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the knowledge product category name

    def clean(self):
        if StgFacilityOwnership.objects.filter(
            translations__name=self.name).count() and not self.owner_id and not \
                self.code:
            raise ValidationError({'name':_('Resource type with the same \
                name exists')})

    def save(self, *args, **kwargs):
        super(StgFacilityOwnership, self).save(*args, **kwargs)


class StgHealthFacility(TranslatableModel):
    STATUS_CHOICES = (
        ('pending', 'Active'),
        ('approved', 'Inactive'),
    )
    # Regular expression to validate phone number entry to international format
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone Number format: '+999999999' maximum 15.")
    facility_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, blank=True,null=False,max_length=45)
    type = models.ForeignKey(StgFacilityType, models.PROTECT,blank=False,
        null=False,verbose_name = 'Facility Type')
    location = models.ForeignKey(StgLocation, models.PROTECT,
        verbose_name = 'Location',default = 1)
    owner = models.ForeignKey(StgFacilityOwnership, models.PROTECT,
        verbose_name = 'facility Ownership')
    infrastructure = models.ManyToManyField(StgFacilityInfrastructure,
        db_table='stg_infrastructure_lookup',blank=True,
        verbose_name = 'Health Infratructures')
    translations = TranslatedFields(
        name = models.CharField(max_length=230,blank=False, null=False,
            verbose_name = 'Facility Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=230,blank=False, null=False,
            verbose_name ='Short Name', default='NotAvailable'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description'), # Field name made lowercase.
        address = models.CharField(max_length=500,blank=True,null=True,
            verbose_name = _('Contact Address')),  # Field name made lowercase.
        email = models.EmailField(unique=True,max_length=250,blank=True,null=True,
            verbose_name = 'Email'),  # Field name made lowercase.
        phone_number = models.CharField(_('Phone Number'),
            validators=[phone_regex], max_length=15, blank=True), # validators should be a list
        year_established = models.IntegerField(default=datetime.now().year,
            verbose_name='Year Established'),
        latitude = models.FloatField(blank=True, null=True),
        longitude = models.FloatField(blank=True, null=True),
        url = models.URLField(blank=True, null=True, max_length=2083,
            verbose_name = 'Web Address'),
    )  # End of translatable fields

    status = models.CharField(max_length=10, choices= STATUS_CHOICES,
        default=STATUS_CHOICES[0][0], verbose_name='Status')
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_health_facility'
        verbose_name = 'Health Facility'
        verbose_name_plural = '  Health Facilities'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the data element name

    def clean(self): # Don't allow end_period to be greater than the start_period.
        import datetime
        if self.year_established > datetime.date.today().year:
            raise ValidationError({'year_established':_(
                'Sorry! The year facility was established cannot be in future!')})

        if StgHealthFacility.objects.filter(
            translations__name=self.name).count() and not self.facility_id and not \
                self.year_published and not self.location:
            raise ValidationError({'name':_('Facility  with the same name exists')})

    def save(self, *args, **kwargs):
        super(StgHealthFacility, self).save(*args, **kwargs)


class StgServiceDomain(TranslatableModel):
    domain_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Theme Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=45,null=True,
            verbose_name = 'Short Name',),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True),
        level = models.IntegerField(default=1,verbose_name='Service Level')
        )
    code = models.CharField(unique=True, max_length=50, blank=True,
            null=True, verbose_name = 'Theme Code')  # Field name made lowercase.
    parent = models.ForeignKey('self',on_delete=models.CASCADE,
        blank=True,null=True,verbose_name = 'Parent Domain')  # Field name made lowercase.
    facilities = models.ManyToManyField(StgHealthFacility,
        db_table='stg_service_domain_members',
        blank=True,verbose_name = 'Health Facilities')  # Field name made lowercase.
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True # must be true to create the model table in mysql
        db_table = 'stg_service_domain'
        verbose_name = 'Service Domain'
        verbose_name_plural = ' Service Domains'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the knowledge product category name

    def clean(self):
        if StgServiceDomain.objects.filter(
            translations__name=self.name).count() and not self.domain_id and not \
                self.code:
            raise ValidationError({'name':_('Domain with the same name exists')})

    def save(self, *args, **kwargs):
        super(StgServiceDomain, self).save(*args, **kwargs)

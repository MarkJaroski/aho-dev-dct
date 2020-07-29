from django.db import models
import uuid
from parler.models import TranslatableModel, TranslatedFields
from publications.models import (StgResourceType,StgKnowledgeProduct,
    StgProductDomain,)
from regions.models import StgLocation
from facilities.models import (StgHealthFacility,)


def make_choices(values):
    return [(v, v) for v in values]


"""
Knowledge Resource proxy model.The def clean (self) method was contributed
by Daniel Mbugua to resolve the issue of parent-child saving issue in the
multi-records entry form.My credits to Mr Mbugua of MSc DCT, UoN-Kenya

"""
class ResourceTypeProxy(StgResourceType):
    class Meta:
        proxy = True
        verbose_name = 'Resource Type'
        verbose_name_plural = ' Resource Types'

    def clean(self):
        pass

class HumanWorkforceResourceProxy(StgKnowledgeProduct):
    class Meta:
        proxy = True
        verbose_name = 'Resource & Guide'
        verbose_name_plural = ' Resources & Guides'

    def clean(self):
        pass


# New model to take care of resource types added 11/05/2019 courtesy of Gift
class StgInstitutionType(TranslatableModel):
    FLAG = ('publications','health_workforce','general',)
    type_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Resource Type Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=230, blank=True, null=True,
            verbose_name = 'Short Name'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description')  # Field name made lowercase.
    )
    code = models.CharField(unique=True, max_length=50, blank=True,
        null=True, verbose_name = 'Code')  # Field name made lowercase.
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_institution_type'
        verbose_name = 'Institution Type'
        verbose_name_plural = 'Institution Types'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the knowledge product category name


class StgTrainingInstitution(TranslatableModel):
    STATUS_CHOICES = ( #choices for approval of indicator data by authorized users
        ('accredited', 'Accredited'),
        ('charterted','Chartered'),
        ('unacredited','Not Accredited'),
        ('pending','Pending Accreditation'),
    )

    institution_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    translations = TranslatedFields(
        name = models.CharField(max_length=230,blank=False, null=False,
            verbose_name = 'Location Name'),  # Field name made lowercase.
        programmes = models.TextField(blank=True, null=True,
            verbose_name = 'Training Programs'),
        level =models.CharField(max_length=150, blank=False,
                null=False,verbose_name = 'Highest Academic Level'),  # Field name made lowercase.
        accreditation = models.CharField(max_length=50, choices= STATUS_CHOICES,
            default=STATUS_CHOICES[0][0], verbose_name='Accreditation Status'),  # Field name made lowercase.
        accreditation_info = models.CharField(max_length=2000, blank=True,
            verbose_name = 'Accreditation Details'),
        language = models.CharField(max_length=50, blank=False,
            verbose_name = 'Teaching Language'),
        address = models.CharField(max_length=500,blank=False,null=False,
            verbose_name = 'Contact Address'),
        posta = models.CharField(max_length=500,blank=True,null=False,
            verbose_name = 'Postal Address'),  # Field name made lowercase.
        email = models.CharField(unique=True,max_length=250,blank=True,null=False,
            verbose_name = 'Email Address'),  # Field name made lowercase.
        latitude = models.FloatField(blank=True, null=True),
        longitude = models.FloatField(blank=True, null=True),
    )
    code = models.CharField(unique=True, max_length=15, blank=True, null=False,
        verbose_name = 'Institution Code')  # Field name made lowercase.
    location = models.ForeignKey(StgLocation, models.PROTECT,blank=False,
        null=False, verbose_name = 'Geographical Location', default='1')  # Field name made lowercase.
    type = models.ForeignKey(StgInstitutionType, models.PROTECT, blank=False,
        null=False, verbose_name = 'Institution Type',default=6)  # Field name made lowercase.
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_traininginstitution'
        verbose_name = 'Institution' # this is important in the display on change details and the add button
        verbose_name_plural = 'Training Institutions'
        ordering = ['code',]

    def __str__(self):
        return self.name #display the location name such as country

    # This function makes sure the location name is unique instead of enforcing unque constraint on DB
    def clean(self): # Don't allow end_period to be greater than the start_period.
        if StgTrainingInstitution.objects.filter(
            translations__name=self.name).count() and not self.institution_id:
            raise ValidationError(
                {'name':_('Training Institution with the this name exists')})

    def save(self, *args, **kwargs):
        super(StgTrainingInstitution, self).save(*args, **kwargs)


class StgHealthWorkforceFacts(TranslatableModel):
    STATUS_CHOICES = (
        ('pending', 'Active'),
        ('approved', 'Inactive'),
    )

    AGGREGATION_TYPE = ('Count','Sum','Average','Standard Deviation',
        'Variance', 'Min', 'max','None')
    fact_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,
        blank=False,null=False, default=uuid.uuid4,editable=False,
        verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, blank=True,null=False,
        max_length=45,verbose_name='ISCO-08 Code')
    institution = models.ForeignKey(StgTrainingInstitution, models.PROTECT,blank=False,
        null=False,verbose_name = 'Highest Institution')
    location = models.ForeignKey(StgLocation, models.PROTECT,
        verbose_name = 'Geographical Location',default = 1)
    facility = models.ForeignKey(StgHealthFacility, models.PROTECT,
        verbose_name = 'Affliation')
    translations = TranslatedFields(
        name = models.CharField(max_length=230,blank=False, null=False,
            verbose_name = 'Cadre (Occupation) Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=230,blank=False, null=False,
            verbose_name ='Cadre Short Name', default='Not Available'),  # Field name made lowercase.
        academic = models.CharField(max_length=500,blank=True,null=True,
            verbose_name = 'Qualification Level'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description')  # Field name made lowercase.
    )  # End of translatable fields
    aggregation_type = models.CharField(max_length=45, verbose_name = 'Aggregate Type',
        choices=make_choices(AGGREGATION_TYPE),default=AGGREGATION_TYPE[0])  # Field name made lowercase.
    status = models.CharField(max_length=10, choices= STATUS_CHOICES,
        default=STATUS_CHOICES[0][0], verbose_name='Status')
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'fact_health_workforce'
        verbose_name = 'Healthworkforce Data'
        verbose_name_plural = '  Healthworkforce Data'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the data element name

    def clean(self): # Don't allow end_period to be greater than the start_period.
        import datetime
        if StgHealthWorkforceFacts.objects.filter(
            translations__name=self.name).count() and not self.fact_id and not \
                self.year_published and not self.location:
            raise ValidationError({'name':_('The same healthworkforce data exists')})

    def save(self, *args, **kwargs):
        super(StgHealthWorkforceFacts, self).save(*args, **kwargs)

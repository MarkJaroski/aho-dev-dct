from django.db import models
import uuid
import datetime
from django.db.models.fields import DecimalField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ # The _ is alias for gettext
from parler.models import TranslatableModel, TranslatedFields
from publications.models import (StgResourceType,StgKnowledgeProduct,
    StgProductDomain,)
from regions.models import StgLocation
from facilities.models import (StgHealthFacility,)
from home.models import (StgDatasource,StgCategoryoption,StgMeasuremethod)

def make_choices(values):
    return [(v, v) for v in values]

YEAR_CHOICES = [(r,r) for r in range(1990, datetime.date.today().year+1)]
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
    code = models.CharField(unique=True, max_length=50, blank=True,
        null=True, verbose_name = 'Code')  # Field name made lowercase.
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Resource Type Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=230, blank=True, null=True,
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
        db_table = 'stg_institution_type'
        verbose_name = 'Institution Type'
        verbose_name_plural = 'Institution Types'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the knowledge product category name


# New model to take care of resource types added 11/05/2019 courtesy of Gift
class StgInstitutionProgrammes(TranslatableModel):
    course_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, max_length=50, blank=True,
        null=True, verbose_name = 'Code')  # Field name made lowercase.
    translations = TranslatedFields(
        name = models.CharField(max_length=230, blank=False, null=False,
            verbose_name = 'Resource Type Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=230, blank=True, null=True,
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
        db_table = 'stg_institution_programme'
        verbose_name = ' Programme'
        verbose_name_plural = 'Training Programmes'
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
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Phone Number format: '+999999999' maximum 15.")
    institution_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,blank=False,null=False,
        default=uuid.uuid4,editable=False, verbose_name = 'Unique Universal ID')
    programmes = models.ManyToManyField(StgInstitutionProgrammes,
        db_table='stg_institution_programs_lookup',blank=True,
        verbose_name = 'Training Programmes')
    translations = TranslatedFields(
        name = models.CharField(max_length=230,blank=False, null=False,
            verbose_name = 'Institution Name'),  # Field name made lowercase.
        faculty =models.CharField(max_length=150, blank=True,null=True,
                verbose_name = 'Faculty Name'),  # Field name made lowercase.
        accreditation = models.CharField(max_length=50, choices= STATUS_CHOICES,
            default=STATUS_CHOICES[0][0], verbose_name='Accreditation Status'),  # Field name made lowercase.
        regulator = models.CharField(max_length=150, blank=True,
                null=True,verbose_name = 'Regulatory Body'),  # Field name made lowercase. # Field name made lowercase.
        accreditation_info = models.CharField(max_length=2000, blank=True,
            verbose_name = 'Accreditation Details'),
        language = models.CharField(max_length=50, blank=True,null=True,
            verbose_name = 'Teaching Language'),
        address = models.CharField(max_length=500,blank=True,null=True,
            verbose_name = 'Contact Address/Person'),
        posta = models.CharField(max_length=500,blank=True,null=True,
            verbose_name = 'Postal Address'),  # Field name made lowercase.
        email = models.EmailField(unique=True,max_length=250,blank=True,
            null=True,verbose_name = 'Email Address'),  # Field name made lowercase.
        phone_number = models.CharField(_('Phone Number'),
            validators=[phone_regex], max_length=15, blank=True), # validators should be a list
        url = models.URLField(blank=True, null=True, max_length=2083,
            verbose_name = 'Web Address'),
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
    def clean(self): # Don't allow end_year to be greater than the start_year.
        if StgTrainingInstitution.objects.filter(
            translations__name=self.name).count() and not self.institution_id:
            raise ValidationError(
                {'name':_('Training Institution with the this name exists')})

    def save(self, *args, **kwargs):
        super(StgTrainingInstitution, self).save(*args, **kwargs)



class StgHealthCadre(TranslatableModel):
    STATUS_CHOICES = ( #choices for approval of indicator data by authorized users
        ('degree', 'Degree'),
        ('diploma', 'Diploma'),
        ('masters','Masters'),
        ('phd','Doctorate'),
        ('certificate','Certificate'),
        ('basic','Basic Education'),

    )
    cadre_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,
        blank=False,null=False, default=uuid.uuid4,editable=False,
        verbose_name = 'Unique Universal ID')
    code = models.CharField(unique=True, blank=True,null=False,
        max_length=45,verbose_name='ISCO-08 Code')
    parent = models.ForeignKey('self', models.PROTECT,blank=True, null=True,
        verbose_name = 'Parent Group',default=1,)
    translations = TranslatedFields(
        name = models.CharField(max_length=230,blank=False, null=False,
            verbose_name = 'Cadre Name'),  # Field name made lowercase.
        shortname = models.CharField(max_length=230,blank=False, null=False,
            verbose_name ='Short Name', default='Not Available'),  # Field name made lowercase.
        academic = models.CharField(max_length=10, choices= STATUS_CHOICES,
            default=STATUS_CHOICES[0][0],verbose_name = 'Qualification'),  # Field name made lowercase.
        description = models.TextField(blank=True, null=True,
            verbose_name = 'Description')  # Field name made lowercase.
    )  # End of translatable fields
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True,
        verbose_name = 'Date Created')
    date_lastupdated = models.DateTimeField(blank=True, null=True, auto_now=True,
        verbose_name = 'Date Modified')

    class Meta:
        managed = True
        db_table = 'stg_health_cadre'
        verbose_name = 'Health Cadre'
        verbose_name_plural = ' Health Cadres'
        ordering = ('code', )

    def __str__(self):
        return self.name #display the data element name

    def clean(self): # Don't allow end_year to be greater than the start_year.
        import datetime
        if StgHealthCadre.objects.filter(
            translations__name=self.name).count() and not self.code:
            raise ValidationError({'name':_('The same occupation/cadre exists')})

    def save(self, *args, **kwargs):
        super(StgHealthCadre, self).save(*args, **kwargs)


class StgHealthWorkforceFacts(models.Model):
    STATUS_CHOICES = ( #choices for approval of indicator data by authorized users
        ('pending', 'Pending'),
        ('approved','Approved'),
        ('rejected','Rejected'),
    )
    AGGREGATION_TYPE = ('Count','Sum','Average','Standard Deviation',
        'Variance', 'Min', 'max','None')
    fact_id = models.AutoField(primary_key=True)
    uuid = uuid = models.CharField(unique=True,max_length=36,
        blank=False,null=False, default=uuid.uuid4,editable=False,
        verbose_name = 'Unique Universal ID')
    cadre_id = models.ForeignKey(StgHealthCadre, models.PROTECT,
        verbose_name = 'Occupation/Cadre',default = 1)  # disallow deletion of a related field
    location = models.ForeignKey(StgLocation, models.PROTECT,
        verbose_name = 'Geographical Location',default = 1)
    categoryoption = models.ForeignKey(StgCategoryoption, models.PROTECT,
        verbose_name = 'Disaggregation Options')  # disallow deletion of a related field
    datasource = models.ForeignKey(StgDatasource, models.PROTECT,blank=False,
        null=False,verbose_name = 'Data Source', default = 1)  # Field name made lowercase.
    measuremethod = models.ForeignKey(StgMeasuremethod, models.PROTECT,blank=True,
        null=True, verbose_name = 'Type of Measure')  # Field name made lowercase.
    value = DecimalField(max_digits=20,decimal_places=2,
        blank=False, null=False, verbose_name = 'Data Value')  # Field name made lowercase.
    start_year = models.IntegerField(null=False,blank=False,
        default=datetime.date.today().year,verbose_name='Start Year')
    end_year  = models.IntegerField(null=False,blank=False,
        default=datetime.date.today().year,verbose_name='Ending Year',)
    period = models.CharField(max_length=10,blank=True,
        null=False, verbose_name = 'Period') #try to concatenate period field
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
        ordering = ('cadre_id', )

    def __str__(self):
         return str(self.cadre_id)
    """
    The purpose of this method is to compare the start_year to the end_year. If the
    start_year is greater than the end_year athe model should show an inlines error
    message and wait until the user corrects the mistake.
    """
    def clean(self): # Don't allow end_year to be greater than the start_year.
        if self.start_year<=1990 or self.start_year > datetime.date.today().year:
            raise ValidationError({'start_year':_(
                'Sorry! Start year cannot be less than 1990 or greater than current Year ')})
        elif self.end_year <=1990 or self.end_year > datetime.date.today().year:
            raise ValidationError({'end_year':_(
                'Sorry! The ending year cannot be lower than the start year or \
                greater than the current Year ')})
        elif self.end_year < self.start_year and self.start_year is not None:
            raise ValidationError({'end_year':_(
                'Sorry! Ending period cannot be lower than the start period. \
                 Please make corrections')})

    """
    The purpose of this method is to concatenate the date that are entered as
    start_year and end_year and save the concatenated value as a string in
    the database ---this is very important to take care of Davy's date complexity
    """
    def get_period(self):
        if self.period is None or (self.start_year and self.end_year):
            if self.start_year == self.end_year:
                period = int(self.start_year)
            else:
                period =str(int(self.start_year))+"-"+ str(int(self.end_year))
        return period


    def save(self, *args, **kwargs):
        self.period = self.get_period()
        super(StgHealthWorkforceFacts, self).save(*args, **kwargs)

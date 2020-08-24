from django.contrib import admin
from parler.admin import TranslatableAdmin
from regions.models import StgLocation
from data_wizard.admin import ImportActionModelAdmin
from data_wizard.sources.models import FileSource,URLSource #customize import sourece
from django.forms import TextInput,Textarea #for customizing textarea row and column size
from commoninfo.admin import OverideImportExport, OverideExport
from .models import (StgCategoryParent,StgCategoryoption,StgMeasuremethod,
    StgValueDatatype,StgDatasource)
from .resources import(DisaggregateCategoryExport,DataSourceExport,
    DisaggregateOptionExport,MeasureTypeExport,DataTypeExport)
from import_export.admin import (ImportExportModelAdmin,
    ImportExportActionModelAdmin,)
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter,
    RelatedOnlyDropdownFilter) #custom import


@admin.register(StgCategoryParent)
class DisaggregateCategoryAdmin(TranslatableAdmin,OverideExport):
    menu_title = "Disagregation Categories"
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = DisaggregateCategoryExport #for export only
    list_display=['name','code','shortname','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('translations__name', 'translations__shortname','code',) #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)


@admin.register(StgCategoryoption)
class DisaggregationAdmin(TranslatableAdmin,OverideExport):
    menu_title = "Category Options"
    fieldsets = (
        ('Disaggregation Attributes', {
                'fields': ('category', 'name','shortname',)
            }),
            ('Detailed Description', {
                'fields': ('description',),
            }),
        )
    resource_class = DisaggregateOptionExport #for export only
    list_display=['name','code','shortname','description','category',]
    list_display_links = ('code', 'name',)
    search_fields = ('translations__name', 'translations__shortname',) #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated',)
    list_filter = (
        ('category',RelatedOnlyDropdownFilter,), #must put this comma for inheritance
    )


@admin.register(StgValueDatatype)
class DatatypeAdmin(TranslatableAdmin,OverideExport):
    menu_title = "Data Types"
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = DataTypeExport
    list_display=['code','name','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('translations__name', 'translations__shortname','code',) #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)

@admin.register(StgDatasource)
class DatasourceAdmin(TranslatableAdmin,OverideExport):
    menu_title = "Data Sources"
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    fieldsets = (
        ('Data source Attributes', {
                'fields': ('name','shortname','level',)
            }),
            ('Detailed Description', {
                'fields': ('description',),
            }),
        )
    resource_class = DataSourceExport #for export only
    list_display=['name','shortname','code','description','level']
    list_display_links = ('code', 'name',)
    search_fields = ('translations__name', 'translations__shortname','code','translations__level') #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated',)


@admin.register(StgMeasuremethod)
class MeasuredAdmin(TranslatableAdmin,OverideExport):
    menu_title = "Indicator Types"
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = MeasureTypeExport
    list_display=['name','code','measure_value','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('translations__name','code',) #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)

# ---------------------------------------------------------------------------------------------
# The following two admin classes are used to customize the Data_Wizard page.
# The classes overrides admin.py in site-packages/data_wizard/sources/
# ---------------------------------------------------------------------------------------------
class FileSourceAdmin(ImportActionModelAdmin):
    def get_queryset(self, request):
    		qs = super().get_queryset(request)
    		if request.user.is_superuser or request.user.groups.filter(
                name__icontains='Admins'):
    			return qs #provide access to all instances/rows of fact data indicators
    		return qs.filter(location=request.user.location)  # provide access to user's country indicator instances
    def formfield_for_foreignkey(self, db_field, request =None, **kwargs):
        if db_field.name == "location":
            if request.user.is_superuser:
                kwargs["queryset"] = StgLocation.objects.filter(
                locationlevel__translations__name__in =['Global','Regional','Country']).order_by(
                    'locationlevel', 'location_id') #superuser can access all countries at level 2 in the database
            elif request.user.groups.filter(name__icontains='Admins'):
                kwargs["queryset"] = StgLocation.objects.filter(
                locationlevel__translations__name__in =['Regional','Country']).order_by(
                    'locationlevel', 'location_id')
            else:
                kwargs["queryset"] = StgLocation.objects.filter(
                    #permissions for user country filter---works as per Davy's request
                    location_id=request.user.location_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    fields = ('location','name','file',)
    list_display=['name','location','date']
admin.site.register(FileSource, FileSourceAdmin)


# This class admin class is used to customize change page for the URL data source
class URLSourceAdmin(ImportActionModelAdmin):
    def get_queryset(self, request):
    		qs = super().get_queryset(request)
    		if request.user.is_superuser or request.user.groups.filter(
                name__icontains='Admins'):
    			return qs #provide access to all instances/rows of fact data indicators
    		return qs.filter(location=request.user.location)  # provide access to user's country indicator instances
    def formfield_for_foreignkey(self, db_field, request =None, **kwargs):
        if db_field.name == "location":
            if request.user.is_superuser:
                kwargs["queryset"] = StgLocation.objects.filter(
                locationlevel__translations__name__in =['Global','Regional','Country']).order_by(
                    'locationlevel', 'location_id') #superuser can access all countries at level 2 in the database
            elif request.user.groups.filter(name__icontains='Admins'):
                kwargs["queryset"] = StgLocation.objects.filter(
                locationlevel__translations__name__in =['Regional','Country']).order_by(
                    'locationlevel', 'location_id')
            else:
                kwargs["queryset"] = StgLocation.objects.filter(
                    #permissions for user country filter---works as per Davy's request
                    location_id=request.user.location_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    fields = ('location','name','url',)
    list_display=['name','location','url','date']
admin.site.register(URLSource,URLSourceAdmin)

from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.forms import TextInput,Textarea #for customizing textarea row and column size
from .models import (StgLocationLevel,StgEconomicZones,StgWorldbankIncomegroups,
    StgSpecialcategorization,StgLocation)
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter,
    RelatedOnlyDropdownFilter) #custom
from commoninfo.admin import OverideExport,OverideImportExport,OverideImport
from .resources import (LocationLevelResourceExport,IncomegroupsResourceExport,
    EconomicZoneResourceExport,SpecialcategorizationResourceExport,
    LocationResourceExport,LocationResourceImport)
from import_export.admin import (ExportMixin, ImportExportModelAdmin,
    ImportExportActionModelAdmin,)
from import_export import resources #This is required to limit the import/export fields 26/10/2018

#the following 3 functions are used to register global actions performed on the data. See actions listbox
def pending (modeladmin, request, queryset):
    queryset.update(comment = 'pending')
pending.short_description = "Mark selected as Pending"

def approved (modeladmin, request, queryset):
    queryset.update (comment = 'approved')
approved.short_description = "Mark selected as Approved"

def rejected (modeladmin, request, queryset):
    queryset.update (comment = 'rejected')
rejected.short_description = "Mark selected as Rejected"

@admin.register(StgLocationLevel)
class RegionAdmin(TranslatableAdmin,OverideExport):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = LocationLevelResourceExport
    list_display=['code','name','type','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('code','name','type') #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)
    list_filter = (
        ('translations__name',DropdownFilter),
    )

@admin.register(StgEconomicZones)
class EconomicBlocksAdmin(TranslatableAdmin,OverideExport):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = EconomicZoneResourceExport
    list_display=['code','name','shortname','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('name','shortname') #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code')


@admin.register(StgWorldbankIncomegroups)
class WBGroupsAdmin(TranslatableAdmin,OverideExport):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = IncomegroupsResourceExport
    list_display=['code','name','shortname','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('code','name',) #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)


@admin.register(StgSpecialcategorization)
class SpecialStatesAdmin(TranslatableAdmin,OverideExport):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    resource_class = SpecialcategorizationResourceExport
    list_display=['code','name','shortname','description',]
    list_display_links = ('code', 'name',)
    search_fields = ('name','shortname',) #display search field
    list_per_page = 15 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code')


@admin.register(StgLocation)
class LocationAdmin(TranslatableAdmin,OverideExport):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(
            name__icontains='Admins'):
            return qs #provide access to all instances/rows of all location, i.e. all AFRO member states
        return qs.filter(location_id=request.user.location_id)#provide the user with specific country details!

    #This function is for filtering location to display regional level only. The database field must be parentid for the dropdown list
    def formfield_for_foreignkey(self, db_field, request =None, **kwargs): #to implement user filtering her
        if db_field.name == "parent":
            if request.user.is_superuser or request.user.groups.filter(
                name__icontains='Admins'):
                kwargs["queryset"] = StgLocation.objects.filter(
                locationlevel__translations__name__in =['Country']).order_by(
                'locationlevel',) #superuser can access all countries at level 2 in the database
            else:
                kwargs["queryset"] = StgLocation.objects.filter(
                    location_id=request.user.location_id) #permissions for user country filter---works as per Davy's request

        if db_field.name == "locationlevel":
            if request.user.is_superuser or request.user.groups.filter(
                name__icontains='Country Admins'):
                kwargs["queryset"] = StgLocation.objects.filter(
                locationlevel__translations__name__in =['Country']).order_by(
                'locationlevel',) #superuser can access all countries at level 2 in the database
            else:
                kwargs["queryset"] = StgLocation.objects.filter(
                    location_id=request.user.location_id) #permissions for user country filter---works as per Davy's request

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
        ('Location Details',{
                'fields': (
                    'locationlevel','name', 'iso_alpha','iso_number','description', )
            }),
            ('Geo-map Info', {
                'fields': ('parent','longitude','latitude', 'cordinate',),
            }),
            ('Socioeconomic Status', {
                'fields': ('wb_income','zone','special',),
            }),
        )

    resource_class = LocationResourceExport
    list_display=['name','code','zone','special',]
    list_display_links = ('code', 'name',) #display as clickable link
    search_fields = ('code','name', 'iso_alpha') #display search field
    list_per_page = 30 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated',)
    list_filter = (
        ('locationlevel',RelatedOnlyDropdownFilter),
        ('parent',RelatedOnlyDropdownFilter),
    )

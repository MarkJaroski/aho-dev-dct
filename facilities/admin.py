from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
import data_wizard # Solution to data import madness that had refused to go
from django.forms import TextInput,Textarea #customize textarea row and column size
from import_export.formats import base_formats
from .models import (StgFacilityType,StgFacilityInfrastructure,
    StgFacilityOwnership,StgHealthFacility,StgServiceDomain)
from commoninfo.admin import OverideImportExport,OverideExport
# from publications.serializers import StgKnowledgeProductSerializer
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter,
    RelatedOnlyDropdownFilter) #custom
from import_export.admin import (ImportExportModelAdmin, ExportMixin,
    ImportExportActionModelAdmin)

#Methods used to register global actions performed on data. See actions listbox
def transition_to_pending (modeladmin, request, queryset):
    queryset.update(comment = 'pending')
transition_to_pending.short_description = "Mark selected as Pending"

def transition_to_approved (modeladmin, request, queryset):
    queryset.update (comment = 'approved')
transition_to_approved.short_description = "Mark selected as Approved"

def transition_to_rejected (modeladmin, request, queryset):
    queryset.update (comment = 'rejected')
transition_to_rejected.short_description = "Mark selected as Rejected"

@admin.register(StgFacilityType)
class FacilityTypeAdmin(TranslatableAdmin):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    list_display=['code','name','description']
    list_display_links =('code', 'name',)
    search_fields = ('code','name',) #display search field
    list_per_page = 30 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)


@admin.register(StgFacilityInfrastructure)
class FacilityInfrastructure (TranslatableAdmin):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    list_display=['code','name','shortname','description']
    list_display_links =('code', 'name',)
    search_fields = ('code','name',) #display search field
    list_per_page = 30 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)


@admin.register(StgFacilityOwnership)
class FacilityOwdership (TranslatableAdmin):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    list_display=['code','name','location','shortname','description','address',]
    list_display_links =('code', 'name',)
    search_fields = ('code','name','shortname',) #display search field
    list_per_page = 30 #limit records displayed on admin site to 15
    exclude = ('date_created','date_lastupdated','code',)


@admin.register(StgServiceDomain)
class ServiceDomainAdmin(TranslatableAdmin,OverideExport):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }

    fieldsets = (
        ('Service Domain Attributes', {
                'fields':('name','shortname','description','parent',) #afrocode may be null
            }),
        ('Service Domain Facilities', {
                'fields':('facilities','level') #afrocode may be null
            }),
        )

    list_display=['name','code','shortname','description','level']
    list_display_links =('code', 'name','shortname',)
    search_fields = ('code','name',) #display search field

    filter_horizontal = ('facilities',) # this should display an inline with multiselect

    exclude = ('date_created','date_lastupdated','code',)
    list_per_page = 30 #limit records displayed on admin site to 15
    list_filter = (
        ('parent',RelatedOnlyDropdownFilter),
        ('facilities',RelatedOnlyDropdownFilter,),# Added 16/12/2019 for M2M lookup
    )


@admin.register(StgHealthFacility)
class FacilityAdmin(TranslatableAdmin,ImportExportModelAdmin,ImportExportActionModelAdmin):
    from django.db import models
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or \
            request.user.groups.filter(pk=1):
            # Provide access to all instances/rows of all location, i.e. all AFRO member states
            return qs
        return qs.filter(location_id=request.user.location_id)#provide user with specific country details!

    """
    Returns available export formats.
    """
    def get_import_formats(self):
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]
    #
    # def get_export_resource_class(self):
    #     return StgKnowledgeProductResourceExport
    #
    # def get_import_resource_class(self):
    #     return StgKnowledgeProductResourceImport

    #  #This function is used to register permissions for approvals. See signals,py
    # def get_actions(self, request):
    #     actions = super(ProductAdmin, self).get_actions(request)
    #     if not request.user.has_perm('resources.approve_stgknowledgeproduct'):
    #        actions.pop('transition_to_approved', None)
    #     if not request.user.has_perm('resources.reject_stgknowledgeproduct'):
    #         actions.pop('transition_to_rejected', None)
    #     if not request.user.has_perm('resources.delete_stgknowledgeproduct'):
    #         actions.pop('delete_selected', None)
    #     return actions
    #
    # def get_export_resource_class(self):
    #     return StgKnowledgeProductResourceExport
    #
    # def get_import_resource_class(self):
    #     return StgKnowledgeProductResourceImport

    fieldsets = (
        ('Facility Attributes', {
                'fields':('name','shortname','type','description','owner') #afrocode may be null
            }),
            ('Infrastructure and Location', {
                'fields': ('location', 'infrastructure','year_established'),
            }),
            ('Contact & Access Details', {
                'fields': ('address','latitude','longitude','email','url',),
            }),
        )

    # def get_location(obj):
    #        return obj.location.name
    # get_location.short_description = 'Location'
    #
    #
    # def get_type(obj):
    #        return obj.type.name
    # get_type.short_description = 'Type'

    # To display the choice field values use the helper method get_foo_display where foo is the field name
    list_display=['code','name','year_established','owner','type','infrastructure',
        'url','address','email','status']
    list_display_links = ['code','name',]
    search_fields = ('name','type__name','location__name',) #display search field
    list_per_page = 30 #limit records displayed on admin site to 30
    actions = [transition_to_pending,transition_to_approved,
        transition_to_rejected]
    exclude = ('date_created','date_lastupdated','code',)
    list_filter = (
        ('location',RelatedOnlyDropdownFilter),
        ('type',RelatedOnlyDropdownFilter),
    )

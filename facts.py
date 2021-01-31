class IndicatorFactArchiveAdmin(OverideExport,ExportActionModelAdmin):
    def get_changelist(self, request, **kwargs):
        return CustomChangeList

    def has_add_permission(self, request): #removes the add button because no data entry is needed
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        ''' Customize add/edit form '''
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(IndicatorFactArchiveAdmin, self).change_view(
            request,object_id,extra_context=extra_context)

    def get_afrocode(obj):
        return obj.indicator.afrocode
    get_afrocode.admin_order_field  = 'indicator__afrocode'  #Lookup to allow column sorting by AFROCODE
    get_afrocode.short_description = 'Indicator Code'  #Renames the column head

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(
            name__icontains='Admin' or request.user.location>=1):
            return qs #provide access to all instances of fact data indicators
        return qs.filter(location=request.user.location)

    # def get_export_resource_class(self):
    #     return AchivedIndicatorResourceExport

    resource_class = IndicatorResourceExport
    list_display=['location', 'indicator',get_afrocode,'period','categoryoption',
        'value_received','string_value','comment',]
    search_fields = ('indicator__translations__name', 'location__translations__name',
        'period','indicator__afrocode') #display search field
    list_per_page = 50 #limit records displayed on admin site to 50
    list_filter = (
        ('location', DropdownFilter,),
        ('indicator', DropdownFilter,),
        ('period',DropdownFilter),
        ('categoryoption',DropdownFilter,),
        ('comment',DropdownFilter),
    )

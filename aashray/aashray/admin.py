from django.contrib import admin
from .models import Contact, PlasmaDonorForm
from django.template.loader import render_to_string
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages

# admin.site.register(Contact)

class ContactAdmin(ImportExportModelAdmin):
    """ Admin Panel for Contact Model """

    list_display = ('id','email','name','subject','answered','date')
    search_fields = ('email','name','subject','message','id')
    list_display_links = ('id','email','subject')
    list_filter = ('answered',)
    list_per_page= 60
    ordering = ('date',)

admin.site.register(Contact,ContactAdmin)

class PlasmaDonorFormAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name','age','email', 'contact', 'bloodGroup', 'answered','verified')
    search_fields = ('bloodGroup','name','age', 'email', 'answered')
    list_display_links = ('name', 'age','email', 'contact', 'bloodGroup' )
    list_filter = ('answered','verified')
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(PlasmaDonorForm,PlasmaDonorFormAdmin)
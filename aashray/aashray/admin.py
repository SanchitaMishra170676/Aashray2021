from django.contrib import admin
from .models import Contact
from django.template.loader import render_to_string
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages

# admin.site.register(Contact)

class ContactAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Queries Model """

    list_display = ('id','email','name','subject','answered','date')
    search_fields = ('email','name','subject','message','id')
    list_display_links = ('id','email','subject')
    list_filter = ('answered',)
    list_per_page= 60
    ordering = ('date',)

admin.site.register(Contact,ContactAdmin)
from django.contrib import admin
from .models import Resource
from django.template.loader import render_to_string
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages

admin.site.register(Resource)

# class ResourceAdmin(ImportExportModelAdmin):
#     """ Admin Panel for  Resource Model """

#     list_display = ('name',)
#     search_fields = ('name',)
#     list_display_links = ('name',)
#     list_per_page= 20   

# admin.site.register(Resource, ResourceAdmin)
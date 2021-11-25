from django.contrib import admin

from apps.companias.models import Compania

# Register your models here.

class CompaniaAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']

admin.site.register(Compania, CompaniaAdmin)
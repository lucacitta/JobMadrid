from django.contrib import admin

from apps.companies.models import Company

# Register your models here.

class CompaniaAdmin(admin.ModelAdmin):
    list_display = ['name', 'size']

admin.site.register(Company, CompaniaAdmin)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/',include('apps.companies.urls')),
    path('populate_DB/',include('apps.populate.urls')),
]

from os import name
from django.urls.conf import path


from .api.views import CompaniesBySize, CompaniesByCreationDate
from .api import views

urlpatterns = [
    path('bysize/', CompaniesBySize.as_view(), name = 'CompaniesBySize'),
    path('bycreation/',CompaniesByCreationDate.as_view(), name = 'CompaniesByCreationDate'),
    path('metrics/',views.industry, name = 'metrics')
]
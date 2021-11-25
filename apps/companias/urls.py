from django.urls.conf import path


from .api.views import CompaniesBySize
from .api import views

urlpatterns = [
    path('bysize/', CompaniesBySize.as_view(), name = 'CompaniesBySize')
]
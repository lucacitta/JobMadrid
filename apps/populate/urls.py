from django.urls.conf import path
from .api import views

urlpatterns = [
    path('',views.populate, name='populate'), #URL para poblar la base de datos con el json
]
from django.urls.conf import path
from . import views

urlpatterns = [
    path('poblar_DB',views.poblacion, name='poblacion')
]
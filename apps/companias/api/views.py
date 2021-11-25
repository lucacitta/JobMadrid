from rest_framework import generics

from .serializers import CompaniesSerializer
from apps.companias.models import Compania

class CompaniesBySize(generics.ListAPIView):

    queryset = Compania.objects.order_by('-sizeProm')
    serializer_class = CompaniesSerializer



class CompaniesByCreationDate(generics.ListAPIView):

    queryset = Compania.objects.order_by('-founded')
    serializer_class = CompaniesSerializer
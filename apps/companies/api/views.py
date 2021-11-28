from django.db.models import Count


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.companies.models import Company
from .serializers import CompaniesSerializer
from .serializers import CompaniesIndustryCount, CompaniesCreationCount, CompaniesSizeCount


class CompaniesBySize(generics.ListAPIView):

    queryset = Company.objects.order_by('-sizeProm')
    serializer_class = CompaniesSerializer


class CompaniesByCreationDate(generics.ListAPIView):

    queryset = Company.objects.order_by('-founded')
    serializer_class = CompaniesSerializer


@api_view(['GET'])
def industry(request):

    ByIndustry = (Company.objects
    .values('industry')
    .annotate(count=Count('industry'))
    .order_by()
    )
    IndustrySerializer = CompaniesIndustryCount(ByIndustry, many = True)

    BySize = (Company.objects
    .values('size')
    .annotate(count=Count('size'))
    .order_by()
    )
    sizeSerializer = CompaniesSizeCount(BySize, many = True)

    byCreation = (Company.objects
    .values('founded')
    .annotate(count=Count('founded'))
    .order_by()
    )
    creationSerializer = CompaniesCreationCount(byCreation, many = True)

    return Response({'CompaniesByIndustry':IndustrySerializer.data,
                    'CompaniesBySize':sizeSerializer.data,
                    'CompaniesByCreation':creationSerializer.data})

from django.db.models import Count

import json
from django.http.response import HttpResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.companias.models import Compania
from apps.companias.api.serializers import CompaniesSerializer, CompaniesIndustryCount

@api_view(['GET'])
def populate(request):
    created = get_from_json(request)
    companies = Compania.objects.all()
    serializer = CompaniesSerializer(companies, many = True)
    return Response({'message':f'Created {created} companies in the DataBase', 'Companies': serializer.data})


def get_from_json(request):
    with open('data.json') as file:
        data = json.load(file)
        x = 0
        for i in data:
            id = data[x]['id']
            website = check(data, x, 'website', 'text')
            name = check(data, x, 'name', 'text')
            founded = check(data, x, 'founded', 'number')
            size = check(data, x, 'size', 'number')
            locality = check(data, x, 'locality', 'text')
            region = check(data, x, 'region', 'text')
            country = check(data, x, 'country', 'text')
            industry = check(data, x, 'industry', 'text')
            linkedin_url = check(data, x, 'linkedin_url', 'text')
            sizeProm = prom(data, x)
            compania = Compania(id, website, name, founded, size, sizeProm, locality, region, country, industry, linkedin_url)
            compania.save()
            x += 1
        return x

def check(data, x, variable, type):
    if x in [316, 477, 486] and variable == 'size':
        return 00000
    else:
        if data[x][variable] == None:
            if type == 'text':
                return 'Desconocido'
            else:
                return 00000
        else:
            return data[x][variable]

def prom(data, x):
    control = check(data, x, 'size', 'number')
    number = []
    if control != 00000:
        for character in data[x]['size'].split('-'):
            if character.isdigit():
                number.append(int(character))
        return (number[0] + number[1])/2
    return 00000






@api_view(['GET'])
def industry(request):
    result = (Compania.objects
    .values('industry')
    .annotate(dcount=Count('industry'))
    .order_by()
    )
    serializer = CompaniesIndustryCount(result, many = True)
    return Response({'CompaniesByIndustry':serializer.data})

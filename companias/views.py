import json
from django.http.response import HttpResponse

from .models import Compania


def poblacion(request):
    with open('data.json') as file:
        data = json.load(file)
        x = 0
        for i in data:
            id = data[x]['id']
            website = data[x]['website']
            name = data[x]['name']
            founded = data[x]['founded']
            size = data[x]['size']
            locality = data[x]['locality']
            region = data[x]['region']
            country = data[x]['country']
            industry = data[x]['industry']
            linkedin_url = data[x]['linkedin_url']

            compania = Compania(id, website, name, founded, size, locality, region, country, industry, linkedin_url)
            compania.save()
            x += 1

    return HttpResponse(f'{x} Compañias cargadas a la DB')
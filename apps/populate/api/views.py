
import json


from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.companies.models import Company
from apps.companies.api.serializers import CompaniesSerializer

'''
Funcionamiento:
    Con el decorador api_view se usa la funcion populate, que llama a get_from_json.
    Dentro de esta se obtiene toda la informacion de json y se analiza por elementos, para luego almacenarlos y crear
        el registro en la DB.
    La funcion check, comprueba los valores faltantes, y los rellena con valores identificables.
    La funcion Prom, calcula el promedio de los tamañosy los verifica

'''



@api_view(['GET'])
def populate(request):
    created = get_from_json(request)
    companies = Company.objects.all()
    serializer = CompaniesSerializer(companies, many = True)
    return Response({'message':f'Created {created} companies in the DataBase', 'Companies': serializer.data})


def get_from_json(request):
    #Primero se carga toda la data
    with open('data.json') as file:
        data = json.load(file)
        x = 0

        #iteramos con un contador y los atributos que necesitamos, siempre verificando con check
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
            company = Company(id, website, name, founded, size, sizeProm, locality, region, country, industry, linkedin_url)
            company.save()
            x += 1
        return x

def check(data, x, variable, type):
    #Estas 3 companias tienen errores de input, por lo que desestimamos su valor

    if x in [316, 477, 486] and variable == 'size':
        return 0
    else:

        #Dependiendo de si la variable es numerica o string le asignamos el valor identificable en caso de faltar.

        if data[x][variable] == None:
            if type == 'text':
                return 'Desconocido'
            else:
                return 0
        else:
            return data[x][variable]

def prom(data, x):
    #primero realizamos el check como siempre
    control = check(data, x, 'size', 'number')

    #Separamos los caracteres con el guion y luego los promediamos, en caso de ser un dato faltante pasamos 0

    number = []
    if control != 00000:
        for character in data[x]['size'].split('-'):
            if character.isdigit():
                number.append(int(character))
        return (number[0] + number[1])/2
    return 0


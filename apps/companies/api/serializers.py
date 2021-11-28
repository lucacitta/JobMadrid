from rest_framework import serializers

from apps.companies.models import Company

'''
Serializador base, es el que maneja toda la informacion de la compañias, solo se evita el promedio, ya que es algo
    que yo agregue a las DB.
'''

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('sizeProm',)


'''
Serializadores del endpoint de metricas, cada uno se encarga de serializar la informacion de los distintos conteos.
'''

class CompaniesIndustryCount(serializers.Serializer):
    industry = serializers.CharField(max_length=40)
    count = serializers.IntegerField()

class CompaniesCreationCount(serializers.Serializer):
    founded = serializers.CharField(max_length=40)
    count = serializers.IntegerField()

class CompaniesSizeCount(serializers.Serializer):
    size = serializers.CharField(max_length=20)
    count = serializers.IntegerField()
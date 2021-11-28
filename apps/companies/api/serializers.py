from rest_framework import serializers

from apps.companies.models import Company

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ('sizeProm',)

class CompaniesIndustryCount(serializers.Serializer):
    industry = serializers.CharField(max_length=40)
    count = serializers.IntegerField()

class CompaniesCreationCount(serializers.Serializer):
    founded = serializers.CharField(max_length=40)
    count = serializers.IntegerField()

class CompaniesSizeCount(serializers.Serializer):
    size = serializers.CharField(max_length=20)
    count = serializers.IntegerField()
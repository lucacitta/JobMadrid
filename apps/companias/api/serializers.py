from rest_framework import fields, serializers

from apps.companias.models import Compania

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compania
        fields = '__all__'

class CompaniesIndustryCount(serializers.Serializer):
    industry = serializers.CharField(max_length=40)
    count = serializers.IntegerField()

class CompaniesCreationCount(serializers.Serializer):
    founded = serializers.CharField(max_length=40)
    count = serializers.IntegerField()
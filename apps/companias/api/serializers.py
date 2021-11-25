from rest_framework import fields, serializers

from apps.companias.models import Compania

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compania
        fields = '__all__'
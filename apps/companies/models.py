from django.db import models

'''
Modelo:
    El modelo fue creado con las especificaciones del json, la unica difencia es que se le agrego un campo sizeProm
        usado para ordenar las empresas por tamaño cuando los rangos no sean iguales.
        (Este campo no esta en los endpoints)
'''

class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    website = models.CharField(max_length=80, null=True, blank=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    founded = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    sizeProm = models.FloatField()
    locality = models.CharField(max_length=30, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    industry = models.CharField(max_length=40, null=True, blank=True)
    linkedin_url = models.CharField(max_length=100, null=True, blank=True)

    verbose_name = 'Compañia'
    verbose_name_plural = 'Compañias'

    def __str__(self):
        return self.id



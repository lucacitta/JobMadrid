from django.db import models


class Compania(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    website = models.CharField(max_length=80, null=True, blank=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    founded = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    locality = models.CharField(max_length=30, null=True, blank=True)
    region = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    industry = models.CharField(max_length=40, null=True, blank=True)
    linkedin_url = models.CharField(max_length=100, null=True, blank=True)

    verbose_name = 'Compañia'
    verbose_name_plural = 'Compañias'

    def __str__(self):
        return self.id



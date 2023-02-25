from django.db import models

class Language(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length = 100)


    def __repr__(self):
        return f"language:{self.name}"


class Country(models.Model):
    class Meta:
        ordering = ['country']
    country = models.CharField(max_length = 500)
    languages = models.ManyToManyField(to = Language)


    def __repr__(self):
        return f"country:{self.country}"
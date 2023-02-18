from django.db import models

class Language(models.Model):
   name = models.CharField(max_length=100)
   
   def __str__(self):
    return self.name

class Country(models.Model):
   country = models.CharField(max_length=500)
   languages = models.ManyToManyField(to=Language)
   
   def __str__(self):
    return self.country
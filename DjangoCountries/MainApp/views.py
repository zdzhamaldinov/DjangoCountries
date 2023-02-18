import json
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Country


def home(request):
    context = {
        "name": "Zaur",
        "email": "test@test.ru",
    }
    return render(request, "home.html", context)


def get_country(request,name):
    try:
        country = Country.objects.get(country=name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Country with name={name} not found")
    context = {
        'country': country
    }
    return render(request, 'country.html', context)


def get_countries_list(request):
    context = {
        "countries_list": Country.objects.all(),
    }
    return render(request, "countries_list.html", context)
    
def get_languages_list(request):
    languages_list = []
    for country in Country.objects.all():
        languages_list += country.languages.split(',')
    context = {
        "languages_list": languages_list,
    }
    return render(request, "languages_list.html", context)
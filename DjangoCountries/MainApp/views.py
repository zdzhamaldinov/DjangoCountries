import json
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound


with open('country-by-languages.json') as f:
    countries_list = json.load(f)


def home(request):
    context = {
        "name": "Zaur",
        "email": "test@test.ru",
    }
    return render(request, "home.html", context)


def get_country(request,name):
    for country in countries_list:
        if country['country'] == name:
            context = {
                "country": country['country'],
                "languages": ', '.join(country['languages']),
            }
            return render(request, "country.html", context)
    return HttpResponseNotFound("NotFound")


def get_countries_list(request):
    context = {
        "countries_list": countries_list,
    }
    return render(request, "countries_list.html", context)
    
def get_languages_list(request):
    languages_list = []
    for country in countries_list:
        languages_list += country['languages']
    context = {
        "languages_list": languages_list,
    }
    return render(request, "languages_list.html", context)
import json
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from MainApp.models import Country, Language


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
        'country': country,
        'languages': country.languages.all(),
    }
    return render(request, 'country.html', context)
    
def get_language(request,name):
    try:
        language = Language.objects.get(name=name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Language with name={name} not found")
    context = {
        'language': language,
        'countries': Country.objects.filter(languages=language),
    }
    return render(request, 'language.html', context)


def get_countries_list(request):
    countries = Country.objects.all()
    letter = request.GET.get("letter")
    if letter:
        countries = countries.filter(country__startswith=letter)
    
    page = request.GET.get("page")
    if not page:
        page = 1
    try:
        page = int(page)
    except:
        page = 1   
    paginator = Paginator(countries, per_page=10)
    page_obj = paginator.get_page(page)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page)

    if paginator.num_pages >= page:
        context = {
            "page": page,
            "letter": letter,
            "page_obj": page_obj,
            "alfabet": ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
        }
        return render(request, "countries_list.html", context)
    else:
        return HttpResponseNotFound(f"Page with number={page} not found")
    
def get_languages_list(request):
    context = {
        "languages_list": Language.objects.all(),
    }
    return render(request, "languages_list.html", context)
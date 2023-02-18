from django.shortcuts import render, HttpResponse


def home(request):
    text = f"""
        <h1>Добро пожаловать!</h1>
    """
    return HttpResponse(text)
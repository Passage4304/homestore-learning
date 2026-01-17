from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict = {
        'title': 'Home - Main',
        'content': "Furniture shop HOME"
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'Home - About',
        'content': "About shop",
        'text_on_page': "We are modern shop with soft and comfortable furniture.",
    }
    return render(request, 'main/about.html', context)

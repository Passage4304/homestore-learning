from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context: dict = {
        'title': 'Home - Main',
        'content': "Furniture shop HOME",
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'Home - About',
        'content': "About shop",
        'text_on_page': "We are modern shop with soft and comfortable furniture.",
    }
    return render(request, 'main/about.html', context)

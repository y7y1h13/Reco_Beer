from django.shortcuts import render, get_object_or_404
from .models import *


def home_url(request):
    beers = Beer.objects.filter(category='test')
    return render(request, 'soju/index.html', {'beers':beers})


def beerDetail(request, beer_name=None):
    beer = get_object_or_404(Beer, name=beer_name)
    return render(request, 'soju/detail.html', {'beer':beer})


def reco_url(request):
    return render(request, 'soju/recommend.html')

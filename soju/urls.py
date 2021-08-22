from django.urls import path

from .views import *

app_name = 'soju'

urlpatterns = [
    path('', home_url, name='home_url'),
    path('reco/', reco_url, name='reco'),
    path('<beer_name>/', beerDetail, name='beerDetail'),

]

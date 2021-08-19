from django.urls import path

from .views import *

app_name = 'soju'

urlpatterns = [
    path('', home_url, name='home'),
    #pk값을 뒤에 붙여서 상세페이지 찾기
    path('<beer_name>/', beerDetail, name='beerDetail'),
    path('reco/', reco_url, name='reco'),

]

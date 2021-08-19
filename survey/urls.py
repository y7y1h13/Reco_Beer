from django.urls import path

from .views import *

app_name = 'survey'
urlpatterns = [
    path('', beer_list, name='search'),
    path('result/', search, name='beer_list'),


]

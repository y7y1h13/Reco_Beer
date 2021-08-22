from django.urls import path

from .views import *

app_name = 'survey'

urlpatterns = [
    path('/', beer_list, name='beer_list'),
    path('result/', search, name='search'),


]

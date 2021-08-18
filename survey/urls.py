from django.urls import path

from .views import *

urlpatterns = [
    path('', search),
    path('search/', survey_result),


]

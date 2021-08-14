from django.shortcuts import render
from .models import *


def save_survey(request):
    category = request.GET.get('category', None)
    ABV = request.GET.get('ABV', None)
    sugar = request.GET.get('sugar', None)

    survey = Survey(
        category=category,
        ABV=ABV,
        sugar=sugar

    )
    survey.save()
    return render(request, 'survey/survey.html')
from django.shortcuts import render, redirect
from .models import *
from soju.models import *


def save_survey(request):
    if request.method == 'GET':
        category = request.GET.get('category', None)
        ABV = request.GET.get('ABV', None)
        sugar = request.GET.get('sugar', None)

        res_data = ''
        if not (category and ABV and sugar):
            res_data = '값을 선택해 주세요!'
        else:
            survey = Survey(
                category=category,
                ABV=ABV,
                sugar=sugar

            )
            survey.save()
            return survey_result(request)
    return render(request, 'survey/survey.html')


def survey_result(request):
    beers = Beer.objects.all()
    return render(request, 'survey/result.html', {'beers': beers})
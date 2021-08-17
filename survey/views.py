from django.shortcuts import render, redirect
from .models import *
from soju.models import *


def save_survey(request):
    if request.method == 'GET':
        category = request.GET.getlist('category', None)
        ABV1 = request.GET.get('ABV1', None)
        ABV2 = request.GET.get('ABV2', None)
        sugar = request.GET.get('sugar', None)
        sanmi = request.GET.get('sanmi', None)

        res_data = ''
        if not (category and ABV1 and ABV2 and sugar):
            res_data = '값을 입력해 주세요!'
        else:
            survey = Survey(
                category=category,
                ABV1=ABV1,
                ABV2=ABV2,
                sugar=sugar,
                sanmi=sanmi

            )
            survey.save()
            return survey_result(request)
    return render(request, 'survey/survey.html')


def survey_result(request):
    beers = Beer.objects.all()
    return render(request, 'survey/result.html', {'beers': beers})

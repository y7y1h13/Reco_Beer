from django.shortcuts import render
from .models import *


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
    return render(request, 'survey/survey.html')
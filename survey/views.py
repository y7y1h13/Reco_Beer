from django.shortcuts import render
from soju.models import *
from survey.models import Survey
from django.db.models.query_utils import Q


def survey_result(request):
    f = request.GET.getlist('f')
    beers = Beer.objects.all()
    if f:
        print(f)
        query = Q()
        for i in f:
            query = query | Q(category__icontains=i)
            beers = beers.filter(query)
    return render(request, 'survey/result.html', {'beers':beers})


def search(request):
    return render(request, 'survey/survey.html')

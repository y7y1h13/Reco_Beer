from django.shortcuts import render
from soju.models import *
from django.db.models.query_utils import Q


def search(request):
    beers = Beer.objects.all()
    query1 = Q()
    query2 = Q()
    query3 = Q()
    a = request.GET.getlist('category')
    b = request.GET.getlist('sanmi')
    c = request.GET.getlist('sugar')
    d = request.GET.get('ABV1')
    e = request.GET.get('ABV2')
    if a:
        for i in a:
            query1 = query1 | Q(category=i)

        beers = beers.filter(query1)
    if b:
        for i in b:
            query2 = query2 | Q(sanmi=i)

        beers = beers.filter(query2)
    if c:
        for i in c:
            query3 = query3 | Q(sugar=i)

        beers = beers.filter(query3)
    if d and e:
        beers = beers.filter(ABV__range=(d, e))

    return render(request, 'survey/result.html', {'beers': beers})


def beer_list(request):
    return render(request, 'survey/survey.html')

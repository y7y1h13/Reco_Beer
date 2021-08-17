from django.shortcuts import render, get_object_or_404
from .models import *


def get_absolute_url(request):
    # 맥주 데이터베이스의 정보를 다 불러와서 담는다.
    beers = Beer.objects.all()

    #적어야함

    return render(request, 'soju/detail.html', {'beers': beers})

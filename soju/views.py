from django.shortcuts import render, get_object_or_404
from .models import *


def get_absolute_url(request, category_slug=None):
    # 최근 카테고리 변수를 초기화
    current_category = None
    # 카테고리 데이터베이스의 정보를 다 불러와서 담는다.
    categories = Category.objects.all()
    # 맥주 데이터베이스의 정보를 다 불러와서 담는다.
    beers = Beer.objects.all()

    if category_slug:
        # 정보를 url로 보낸다. Category의 전체 정보와 slug를 전송
        current_category = get_object_or_404(Category, slug=category_slug)
        # 카테고리를 선택하면 그 카테고리에 속해있는 맥주를 필터링해서 저장
        beers = Beer.filter(category=current_category)

        return render(request, 'soju/detail.html', {'beers': beers})

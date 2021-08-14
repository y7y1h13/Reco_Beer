from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    # 관리자 페이지에 보여질 내용
    list_display = ['name', 'slug']
    # 이름을 적으면 자동으로 슬러그가 이름으로 생성
    prepopulated_fields = {'slug': ['name']}


# 앱등록
admin.site.register(Category, CategoryAdmin)


class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    # 필터는 나중에 필요하면 추가
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Beer, BeerAdmin)

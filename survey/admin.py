from django.contrib import admin
from .models import *


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('category1', 'category2', 'category3', 'category4', 'ABV1', 'ABV2', 'sugar')


admin.site.register(Survey, SurveyAdmin)


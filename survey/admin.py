from django.contrib import admin
from .models import *

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('category', 'ABV1', 'ABV2', 'sugar')


admin.site.register(Survey, SurveyAdmin)
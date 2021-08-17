from django.contrib import admin
from .models import *


class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


admin.site.register(Beer, BeerAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name']


admin.site.register(User, UserAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_like']


admin.site.register(Like, LikeAdmin)


class UserstarAdmin(admin.ModelAdmin):
    list_display = ['name', 'name']


admin.site.register(Userstar, UserstarAdmin)

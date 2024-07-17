from django.contrib import admin

from meals.models import MenuBannerModel, MealCategoryModel, MealModel


@admin.register(MenuBannerModel)
class MenuBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(MealCategoryModel)
class MealCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(MealModel)
class MealModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'created_at']
    list_filter = ['title', 'category', 'price', 'created_at']
    search_fields = ['title', 'category']

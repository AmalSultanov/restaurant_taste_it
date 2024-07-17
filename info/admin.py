from django.contrib import admin

from info.models import (AboutBannerModel, AboutInfoModel,
                         AboutStatisticsPhotoModel, AboutStatisticsModel,
                         StaffBannerModel, StaffModel)


@admin.register(AboutBannerModel)
class AboutBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(AboutInfoModel)
class AboutInfoModelAdmin(admin.ModelAdmin):
    list_display = ['upper_title', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['upper_title', 'title']


@admin.register(AboutStatisticsPhotoModel)
class AboutStatisticsPhotoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']


@admin.register(AboutStatisticsModel)
class AboutStatisticsModelAdmin(admin.ModelAdmin):
    list_display = ['stat_number', 'stat_title', 'created_at']
    list_filter = ['stat_title', 'created_at']
    search_fields = ['stat_title']


@admin.register(StaffBannerModel)
class StaffBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'created_at']
    list_filter = ['name', 'role', 'created_at']
    search_fields = ['name', 'role']

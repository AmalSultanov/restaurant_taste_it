from django.contrib import admin

from pages.models import (HomeBannerModel, CommentBannerModel, CommentModel,
                          ContactBannerModel, ContactInfoModel, ContactModel,
                          HomeInfoModel)


@admin.register(HomeBannerModel)
class HomeBannerModelAdmin(admin.ModelAdmin):
    list_display = ['upper_title', 'middle_title', 'lower_title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['upper_title', 'middle_title', 'lower_title']


@admin.register(CommentBannerModel)
class CommentBannerModelAdmin(admin.ModelAdmin):
    list_display = ['upper_title', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['upper_title', 'title']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'created_at']
    list_filter = ['role']
    search_fields = ['name', 'role', 'description']


@admin.register(ContactBannerModel)
class ContactBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(ContactInfoModel)
class ContactInfoModelAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'created_at']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'subject']


@admin.register(HomeInfoModel)
class HomeInfoModelAdmin(admin.ModelAdmin):
    list_display = ['upper_title', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['upper_title', 'title']

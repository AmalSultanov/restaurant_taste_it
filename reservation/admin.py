from django.contrib import admin

from reservation.models import ReservationBannerModel, ReservationModel


@admin.register(ReservationBannerModel)
class ReservationBannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'created_at']
    list_filter = ['date', 'time', 'created_at']
    search_fields = ['name']

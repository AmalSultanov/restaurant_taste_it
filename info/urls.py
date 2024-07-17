from django.urls import path

from info.views import AboutTemplateView, StaffListView, load_more_staff

app_name = 'info'

urlpatterns = [
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('load/', load_more_staff, name='load'),
]

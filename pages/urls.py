from django.urls import path

from pages.views import HomeTemplateView, ContactsCreateView

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
]

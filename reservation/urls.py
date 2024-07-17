from django.urls import path

from reservation.views import ReservationCreateView

app_name = 'reservation'

urlpatterns = [
    path('', ReservationCreateView.as_view(), name='reservation'),
]

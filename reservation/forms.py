from django import forms

from reservation.models import ReservationModel


class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['name', 'email', 'phone', 'date', 'time', 'number_of_people']

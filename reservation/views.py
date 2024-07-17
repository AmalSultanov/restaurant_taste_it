from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView

from pages.models import HomeInfoModel
from reservation.forms import ReservationModelForm
from utils import get_referer_title


class ReservationCreateView(SuccessMessageMixin, CreateView):
    template_name = 'reservation.html'
    form_class = ReservationModelForm
    success_message = 'You have successfully booked a table!'

    def get_success_url(self):
        return reverse('reservation:reservation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_info'] = HomeInfoModel.objects.all()
        context['referer_title'] = get_referer_title(self.request)

        return context

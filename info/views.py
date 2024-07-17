from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView

from info.models import (AboutBannerModel, AboutInfoModel,
                         AboutStatisticsPhotoModel, AboutStatisticsModel,
                         StaffModel, StaffBannerModel)
from utils import get_referer_title


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_banners'] = AboutBannerModel.objects.all()
        context['referer_title'] = get_referer_title(self.request)
        context['about_info'] = AboutInfoModel.objects.all()
        context['statistics_photos'] = AboutStatisticsPhotoModel.objects.all()
        context['statistics'] = AboutStatisticsModel.objects.all()

        return context


class StaffListView(ListView):
    template_name = 'staff.html'

    def get_queryset(self):
        return StaffModel.objects.all()[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_banners'] = StaffBannerModel.objects.all()
        context['referer_title'] = get_referer_title(self.request)
        context['staff_list'] = StaffModel.objects.all()

        return context


def load_more_staff(request):
    try:
        offset = int(request.GET['offset'])
    except KeyError:
        offset = 0

    limit = int(request.GET['limit'])
    staff_list = StaffModel.objects.all()[offset:offset + limit]
    staff_data = [
        {
            'image': staff.image.url,
            'name': staff.name,
            'role': staff.role,
            'description': staff.description
        } for staff in staff_list]
    t = render_to_string('staff_list.html', {'staff_list': staff_data})

    return JsonResponse({'staff_list': t})

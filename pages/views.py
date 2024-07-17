from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from info.models import StaffModel
from meals.models import MealCategoryModel, MealModel
from pages.forms import ContactModelForm
from pages.models import (HomeBannerModel, CommentBannerModel, CommentModel,
                          HomeInfoModel, ContactBannerModel, ContactInfoModel)
from utils import get_referer_title


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_banners'] = HomeBannerModel.objects.all()
        context['referer_title'] = get_referer_title(self.request)
        context['categories'] = MealCategoryModel.objects.all()
        context['category_meals'] = {
            category: MealModel.objects.filter(
                category=category
            ) for category in context['categories']
        }
        context['comment_banners'] = CommentBannerModel.objects.all()
        context['comments'] = CommentModel.objects.all()
        context['staff_list'] = StaffModel.objects.all()[:4]
        context['home_info'] = HomeInfoModel.objects.all()

        return context


class ContactsCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_banners'] = ContactBannerModel.objects.all()
        context['referer_title'] = get_referer_title(self.request)
        context['contact_info'] = ContactInfoModel.objects.all()

        return context

from django.views.generic import ListView

from meals.models import MealModel, MenuBannerModel, MealCategoryModel
from utils import get_referer_title


class MealListView(ListView):
    template_name = 'menu.html'

    def get_queryset(self):
        return MealModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_banners'] = MenuBannerModel.objects.all()
        context['referer_title'] = get_referer_title(self.request)
        context['categories'] = MealCategoryModel.objects.all()
        context['meals'] = MealModel.objects.all()
        context['category_meals'] = {
            category: MealModel.objects.filter(
                category=category
            ) for category in context['categories']
        }

        return context

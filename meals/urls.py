from django.urls import path

from meals.views import MealListView

app_name = 'meals'

urlpatterns = [
    path('', MealListView.as_view(), name='meals'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls', namespace='meals')),
    path('info/', include('info.urls', namespace='info')),
    path('reservation/', include('reservation.urls',
                                 namespace='reservation')),
    path('', include('pages.urls', namespace='pages'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

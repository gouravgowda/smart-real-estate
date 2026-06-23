from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import get_properties, contact_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/properties/', get_properties, name='properties'),
    path('api/contact/', contact_request),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
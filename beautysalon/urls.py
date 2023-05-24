from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from beauty.views import index, service, service_finally, dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('dashboard/', dashboard, name='dashboard')
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

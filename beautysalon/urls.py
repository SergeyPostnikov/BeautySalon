from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from beauty.views import index, service, service_finally, dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='admin/login.html')),
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('dashboard/', dashboard, name='dashboard')
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from beauty.views import index, service, service_finally, dashboard, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='admin/login.html')),
    path('logout', logout, name='logout'),
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('dashboard/', dashboard, name='dashboard')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

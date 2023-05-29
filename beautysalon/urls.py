from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from beauty import views
from django.conf import settings

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='admin/login.html')),
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('service_finally/', views.service_finally, name='service_finally'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('success/<pk>', views.payment_success, name='payment_success'),
    path('payment/<pk>', views.payment, name='payment'),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]

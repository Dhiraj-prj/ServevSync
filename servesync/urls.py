from django.contrib import admin
from django.urls import path, include

from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('login/', views.login_page, name='login'),
    path('worker_login/', views.worker_login, name='worker_login'),
    path('hirer_login/', views.hirer_login, name='hirer_login'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
URL configuration for courseapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings#media yüklemesi için 
from django.conf.urls.static import static#media yüklemesi için
from django.contrib import admin
from django.urls import path, include #burada dahil etme(include) ktüphanesini ekledik




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wejegeh.urls')),
    path('kr/', include('kr.urls')),
    path('en/', include('en.urls')),
   
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#DİKKAT:static dosyaları için aşağıdaki yukarıdaki ise MEDİA için

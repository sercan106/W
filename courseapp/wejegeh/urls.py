from django.urls import path
from . import views #response için görüntü dosyasına yönlendirdik






urlpatterns = [
    path('', views.index),
    path('ev', views.ev), 
    path('ev/<slug:slug>/', views.ev_son, name='ev_son'), 
    path('yayıncılık', views.yayıncılık),
    path('yayıncılık/<slug:slug>/', views.yayıncılık_son, name='yayıncılık_son'), 
    path('hakkımızda', views.hakkımızda),   
    path('program', views.program), 
    path('program/<slug:slug>/', views.program_detail, name='program_detail'),
    path('program/<str:kategori>/<slug:slug>/', views.program_etkinlik, name='program_etkinlik'),
    path('logo', views.logo), 
    path('projeler', views.projeler),
    path('projeler/<slug:slug>/', views.proje, name='proje'),
    path('projeler/<str:kategori>/<slug:slug>/', views.proje_etkinlik, name='proje_etkinlik'),
    path('arşiv/<str:kategori>/<str:kategori2>/', views.arşiv_detay, name='arşiv_detay'),
    path('arşiv', views.arşiv),
    path('search_results/', views.search_results, name='search_results'),
    path('takvim', views.takvim, name='takvim'),



]



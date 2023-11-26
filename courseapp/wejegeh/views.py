import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
#from wejegeh.forms import UrunForm     #hesap klasörünün altındakı forms.py kategoriyi import ettik
from .models import Program_Anasayfa ,Program_Etkinlik,Proje_anasayfa,Proje_Etkinlik
from .models import Yıl,Tür,Alan,Photo,Ev_Yayıncılık,Anasayfa
import random #rastgele sayı üretmek için
import os
from django.contrib.auth.decorators import login_required #loginmi kontrolleri için
from django.contrib import messages
import datetime
# # Create your views here.


def ev(request):
    veri = Anasayfa.objects.filter(name='Ev')
    return render(request, 'wejegeh/ev_ara.html', {'ev': veri})

def ev_son(request, slug):
    veri = get_object_or_404(Ev_Yayıncılık, ust_kategori__slug_tr=slug)  # burada slug_tr'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'wejegeh/ev.html', {'ev': veri})

def yayıncılık_son(request, slug):
    veri = get_object_or_404(Ev_Yayıncılık, ust_kategori__slug_tr=slug)  # burada slug_tr'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'wejegeh/yayıncılık.html', {'yayıncılık': veri})

def yayıncılık(request):
    veri = Anasayfa.objects.filter(name='Yayıncılık')
    return render(request, 'wejegeh/yayıncılık_ara.html', {'yayıncılık': veri})



def index(request):
    program_takvim=Program_Etkinlik.objects.filter(active_takvim=True)
    proje_takvim=Proje_Etkinlik.objects.filter(active_takvim=True)
    takvim=list(proje_takvim) + list(program_takvim)
    takvim_sıralı=sorted(takvim, key=lambda x: x.tarih, reverse=False)
    
    program=Program_Etkinlik.objects.filter(active_vitrin=True)
    proje=Proje_Etkinlik.objects.filter(active_vitrin=True)
    etkinlikler = list(program) + list(proje)
    etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=False)
    return render(request, 'wejegeh/index.html',{'program': program,
                                                'proje': proje,
                                                'etkinlikler_sirali':etkinlikler_sirali, 
                                                                           
                                                'takvimprogram': program_takvim,
                                                'takvimproje': proje_takvim,
                                                'takvim_sıralı':takvim_sıralı, 
                                                
                                                                 })






def program(request):
   return render(request, 'wejegeh/program.html')


def program_detail(request,slug):
    print(slug)
    program = get_object_or_404(Program_Anasayfa, slug_tr=slug)  # burada slug_tr'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    altkategori=Program_Etkinlik.objects.filter(Ust_kategori=program)
    return render(request, 'wejegeh/program_ara.html', {'program': program,
                                                       'altkategori': altkategori})

def program_etkinlik(request,kategori,slug):
    program = get_object_or_404(Program_Etkinlik, slug_tr=slug)  # burada slug_tr'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'wejegeh/program_etkinlik.html', {'program': program})

def projeler(request):
    return render(request, 'wejegeh/projeler.html')

def proje(request,slug):
    program = get_object_or_404(Proje_anasayfa, slug_tr=slug)  # burada slug_tr'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    altkategori=Proje_Etkinlik.objects.filter(Ust_kategori=program)
    return render(request, 'wejegeh/proje_ara.html', {'program': program,
                                                      'altkategori': altkategori})

def logo(request):
    return render(request, 'wejegeh/logolar.html')

def proje_etkinlik(request,kategori,slug):
    program = get_object_or_404(Proje_Etkinlik, slug_tr=slug)  # burada slug_tr'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'wejegeh/proje_son.html', {'program': program})


def hakkımızda(request):
    return render(request, 'wejegeh/hakkımızda.html')



def arşiv(request):
    yıl = Yıl.objects.all().order_by('yıl')
    alan = Alan.objects.all()
    tür = Tür.objects.all()
    return render(request, 'wejegeh/arşiv.html',{'yıl':yıl,
                                                 'alan':alan,
                                                 'tür':tür
                                                  })
def arşiv_detay(request,kategori,kategori2):
    if kategori=="yıl":
        program=Program_Etkinlik.objects.filter(tarih__year=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(tarih__year=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
        
        
    elif kategori=="tür":
        program=Program_Etkinlik.objects.filter(tür__tür_tr=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(tür__tür_tr=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
        
        
    elif kategori=="arşiv seçkisi":
        program=Program_Etkinlik.objects.filter(arşiv_seçkisi=True).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(arşiv_seçkisi=True).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
                
        
    else :
        program=Program_Etkinlik.objects.filter(alan__alan_tr=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(alan__alan_tr=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        

    return render(request, 'wejegeh/arşiv_detay.html',{'program': program,
                                                        'proje': proje,
                                                        'kategori': kategori2, 
                                                        'etkinlikler_sirali':etkinlikler_sirali,                                                  
                                                       })





def search_results(request):
    query = request.GET.get('q')
    if query:
        if query.isdigit() and 1900 <= int(query) <= 2100:  # Eğer query bir yıl ise
            program=Program_Etkinlik.objects.filter(tarih__year=query)
            proje=Proje_Etkinlik.objects.filter(tarih__year=query)
            etkinlikler=list(program) + list(proje)
            etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        else:  # Eğer query bir yıl değilse
            program = Program_Etkinlik.objects.filter(metin_tr__icontains=query)
            proje = Proje_Etkinlik.objects.filter(proje_içerik__metin_tr__icontains=query).distinct()#yinelemeyi engelemek için
            etkinlikler=list(program) + list(proje)
            etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
    else:
        program = Program_Etkinlik.objects.none()
        proje = Proje_Etkinlik.objects.none()

    return render(request, 'wejegeh/search_results.html', {'program': program, 
                                                           'proje': proje,
                                                           'etkinlikler_sirali':etkinlikler_sirali,
                                                           })


def takvim(request):
   return render(request, 'wejegeh/takvim.html')

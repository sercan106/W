import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
#from wejegeh.forms import UrunForm     #hesap klasörünün altındakı forms.py kategoriyi import ettik
from wejegeh.models import Program_Anasayfa ,Program_Etkinlik,Proje_anasayfa,Proje_Etkinlik
from wejegeh.models import Yıl,Tür,Alan,Photo,Ev_Yayıncılık,Anasayfa
import random #rastgele sayı üretmek için
import os
from django.contrib.auth.decorators import login_required #loginmi kontrolleri için
from django.contrib import messages
import datetime
# # Create your views here.


def evv(request):
    veri = Anasayfa.objects.filter(name='Ev')
    return render(request, 'kurdî/ev_ara.html', {'ev': veri})

def ev_sonn(request, slug):
    veri = get_object_or_404(Ev_Yayıncılık, ust_kategori__slug_ku=slug)  # burada slug_ku'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'kurdî/ev.html', {'ev': veri})

def yayıncılık_sonn(request, slug):
    veri = get_object_or_404(Ev_Yayıncılık, ust_kategori__slug_ku=slug)  # burada slug_ku'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'kurdî/yayıncılık.html', {'yayıncılık': veri})

def yayıncılıkk(request):
    veri = Anasayfa.objects.filter(name='Yayıncılık')
    return render(request, 'kurdî/yayıncılık_ara.html', {'yayıncılık': veri})



def indexx(request):
    program_takvim=Program_Etkinlik.objects.filter(active_takvim=True)
    proje_takvim=Proje_Etkinlik.objects.filter(active_takvim=True)
    takvim=list(proje_takvim) + list(program_takvim)
    takvim_sıralı=sorted(takvim, key=lambda x: x.tarih, reverse=True) #reverse=False ters sıralama yapar
    
   
    
    program=Program_Etkinlik.objects.filter(active_anasayfa=True)
    proje=Proje_Etkinlik.objects.filter(active_anasayfa=True)
    etkinlikler = list(program) + list(proje)
    etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
    return render(request, 'kurdî/index.html',{'program': program,
                                                'proje': proje,
                                                'etkinlikler_sirali':etkinlikler_sirali, 
                                                                           
                                                'takvimprogram': program_takvim,
                                                'takvimproje': proje_takvim,
                                                'takvim_sıralı':takvim_sıralı,
                                                                 })







def programm(request):
   return render(request, 'kurdî/program.html')


def program_detaill(request,slug):
    print(slug)
    program = get_object_or_404(Program_Anasayfa, slug_ku=slug)  # burada slug_ku'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    altkategori=Program_Etkinlik.objects.filter(Ust_kategori=program)
    return render(request, 'kurdî/program_ara.html', {'program': program,
                                                       'altkategori': altkategori})

def program_etkinlikk(request,kategori,slug):
    program = get_object_or_404(Program_Etkinlik, slug_ku=slug)  # burada slug_ku'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'kurdî/program_etkinlik.html', {'program': program})

def projelerr(request):
    return render(request, 'kurdî/projeler.html')

def projee(request,slug):
    program = get_object_or_404(Proje_anasayfa, slug_ku=slug)  # burada slug_ku'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    altkategori=Proje_Etkinlik.objects.filter(Ust_kategori=program)
    return render(request, 'kurdî/proje_ara.html', {'program': program,
                                                      'altkategori': altkategori})

def logoo(request):
    return render(request, 'kurdî/logolar.html')

def proje_etkinlikk(request,kategori,slug):
    program = get_object_or_404(Proje_Etkinlik, slug_ku=slug)  # burada slug_ku'yi kullandım, slug_ku veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'kurdî/proje_son.html', {'program': program})


def hakkımızdaa(request):
    return render(request, 'kurdî/hakkımızda.html')



def arşivv(request):
    yıl = Yıl.objects.all().order_by('yıl')
    alan = Alan.objects.all()
    tür = Tür.objects.all()
    return render(request, 'kurdî/arşiv.html',{'yıl':yıl,
                                                 'alan':alan,
                                                 'tür':tür
                                                  })
    
    
    
    
    
    
    
    
 

def arşiv_detayy(request,kategori,kategori2):
    if kategori=="sal":
        program=Program_Etkinlik.objects.filter(tarih__year=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(tarih__year=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
        
        
    elif kategori=="cure":
        program=Program_Etkinlik.objects.filter(tür__tür_ku=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(tür__tür_ku=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
        
        
    elif kategori=="bijareya arşîvê":
        program=Program_Etkinlik.objects.filter(arşiv_seçkisi=True).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(arşiv_seçkisi=True).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
                
        
    else :
        program=Program_Etkinlik.objects.filter(alan__alan_ku=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(alan__alan_ku=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        

    return render(request, 'kurdî/arşiv_detay.html',{'program': program,
                                                        'proje': proje,
                                                        'kategori': kategori2, 
                                                        'etkinlikler_sirali':etkinlikler_sirali,                                                  
                                                       })














def search_resultss(request):
    query = request.GET.get('q')
    if query:
        if query.isdigit() and 1900 <= int(query) <= 2100:  # Eğer query bir yıl ise
            program=Program_Etkinlik.objects.filter(tarih__year=query)
            proje=Proje_Etkinlik.objects.filter(tarih__year=query)
            etkinlikler=list(program) + list(proje)
            etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        else:  # Eğer query bir yıl değilse
            program = Program_Etkinlik.objects.filter(metin_ku__icontains=query)
            proje = Proje_Etkinlik.objects.filter(proje_içerik__metin_ku__icontains=query).distinct()#yinelemeyi engelemek için
            etkinlikler=list(program) + list(proje)
            etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
    else:
        program = Program_Etkinlik.objects.none()
        proje = Proje_Etkinlik.objects.none() 

    return render(request, 'kurdî/search_results.html', {'program': program,
                                                         'proje': proje,
                                                         'etkinlikler_sirali':etkinlikler_sirali,
                                                         })


def takvimm(request):
   return render(request, 'kurdî/takvim.html')


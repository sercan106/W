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


def evvv(request):
    veri = Anasayfa.objects.filter(name='Ev')
    return render(request, 'english/ev_ara.html', {'ev': veri})

def ev_sonnn(request, slug):
    veri = get_object_or_404(Ev_Yayıncılık, ust_kategori__slug_en=slug)  # burada slug_en'yi kullandım, slug_en veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'english/ev.html', {'ev': veri})

def yayıncılık_sonnn(request, slug):
    veri = get_object_or_404(Ev_Yayıncılık, ust_kategori__slug_en=slug)  # burada slug_en'yi kullandım, slug_en veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'english/yayıncılık.html', {'yayıncılık': veri})

def yayıncılıkkk(request):
    veri = Anasayfa.objects.filter(name='Yayıncılık')
    return render(request, 'english/yayıncılık_ara.html', {'yayıncılık': veri})



def indexxx(request):
    program_takvim=Program_Etkinlik.objects.filter(active_takvim=True)
    proje_takvim=Proje_Etkinlik.objects.filter(active_takvim=True)
    takvim=list(proje_takvim) + list(program_takvim)
    takvim_sıralı=sorted(takvim, key=lambda x: x.tarih, reverse=False) #reverse=False ters sıralama yapar
    
    
    program=Program_Etkinlik.objects.filter(active_vitrin=True)
    proje=Proje_Etkinlik.objects.filter(active_vitrin=True)
    etkinlikler = list(program) + list(proje)
    etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=False)
    return render(request, 'english/index.html',{'program': program,
                                                'proje': proje,
                                                'etkinlikler_sirali':etkinlikler_sirali, 
                                                                           
                                                'takvimprogram': program_takvim,
                                                'takvimproje': proje_takvim,
                                                'takvim_sıralı':takvim_sıralı,
                                                                 })









def programmm(request):
   return render(request, 'english/program.html')


def program_detailll(request,slug):
    print(slug)
    program = get_object_or_404(Program_Anasayfa, slug_en=slug)  # burada slug_en'yi kullandım, slug_en veya slug_en'yi de kullanabilirsiniz.
    altkategori=Program_Etkinlik.objects.filter(Ust_kategori=program)
    return render(request, 'english/program_ara.html', {'program': program,
                                                       'altkategori': altkategori})

def program_etkinlikkk(request,kategori,slug):
    program = get_object_or_404(Program_Etkinlik, slug_en=slug)  # burada slug_en'yi kullandım, slug_en veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'english/program_etkinlik.html', {'program': program})

def projelerrr(request):
    return render(request, 'english/projeler.html')

def projeee(request,slug):
    program = get_object_or_404(Proje_anasayfa, slug_en=slug)  # burada slug_en'yi kullandım, slug_en veya slug_en'yi de kullanabilirsiniz.
    altkategori=Proje_Etkinlik.objects.filter(Ust_kategori=program)
    return render(request, 'english/proje_ara.html', {'program': program,
                                                      'altkategori': altkategori})

def logooo(request):
    return render(request, 'english/logolar.html')

def proje_etkinlikkk(request,kategori,slug):
    program = get_object_or_404(Proje_Etkinlik, slug_en=slug)  # burada slug_en'yi kullandım, slug_en veya slug_en'yi de kullanabilirsiniz.
    return render(request, 'english/proje_son.html', {'program': program})


def hakkımızdaaa(request):
    return render(request, 'english/hakkımızda.html')



def arşivvv(request):
    yıl = Yıl.objects.all().order_by('yıl')
    alan = Alan.objects.all()
    tür = Tür.objects.all()
    return render(request, 'english/arşiv.html',{'yıl':yıl,
                                                 'alan':alan,
                                                 'tür':tür
                                                  })
    
    
    
    
    
    
    
    
 
def arşiv_detayyy(request,kategori,kategori2):
    if kategori=="Year":
        program=Program_Etkinlik.objects.filter(tarih__year=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(tarih__year=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
        
        
    elif kategori=="Type":
        program=Program_Etkinlik.objects.filter(tür__tür_en=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(tür__tür_en=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
        
        
    elif kategori=="Featured Archive":
        program=Program_Etkinlik.objects.filter(arşiv_seçkisi=True).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(arşiv_seçkisi=True).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        
                
        
    else :
        program=Program_Etkinlik.objects.filter(alan__alan_en=kategori2).order_by("-tarih")
        proje=Proje_Etkinlik.objects.filter(alan__alan_en=kategori2).order_by("-tarih")
        etkinlikler = list(program) + list(proje)
        etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        

    return render(request, 'english/arşiv_detay.html',{'program': program,
                                                        'proje': proje,
                                                        'kategori': kategori2, 
                                                        'etkinlikler_sirali':etkinlikler_sirali,                                                  
                                                       })
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



def search_resultsss(request):
    query = request.GET.get('q')
    if query:
        if query.isdigit() and 1900 <= int(query) <= 2100:  # Eğer query bir yıl ise
            program=Program_Etkinlik.objects.filter(tarih__year=query)
            proje=Proje_Etkinlik.objects.filter(tarih__year=query)
            etkinlikler=list(program) + list(proje)
            etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)
        else:  # Eğer query bir yıl değilse
            program = Program_Etkinlik.objects.filter(metin_en__icontains=query)
            proje = Proje_Etkinlik.objects.filter(proje_içerik__metin_en__icontains=query).distinct()#yinelemeyi engelemek için
            etkinlikler=list(program) + list(proje)
            etkinlikler_sirali = sorted(etkinlikler, key=lambda x: x.tarih, reverse=True)            
    else:
        program = Program_Etkinlik.objects.none()
        proje = Proje_Etkinlik.objects.none()

    return render(request, 'english/search_results.html', {'program': program,
                                                           'proje': proje,
                                                           'etkinlikler_sirali':etkinlikler_sirali,
                                                           })


def takvimmm(request):
   return render(request, 'english/takvim.html')















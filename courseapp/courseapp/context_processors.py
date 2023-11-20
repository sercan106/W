from wejegeh.models import Takvim, Program_Anasayfa,Logos,Proje_anasayfa,Hakkimizda,Settings,Slide_index,Adres,Anasayfa
# from wejegeh.models import 



def takvim(request):
    veri =  Takvim.objects.all()
    return {
        'takvim': veri #Genel temlateye takvim ismi ile döndürdük
    }

def anasayfa(request):
    veri =  Anasayfa.objects.all()
    return {
        'anasayfa': veri #Genel temlateye anasayfa ismi ile döndürdük
    }




def photoss(request):
    veri =  Slide_index.objects.all()
    return {
        'photoss': veri #Genel temlateye photoss ismi ile döndürdük
    }

 
def program_anasayfa(request):
    veri = Program_Anasayfa.objects.all()
    return {
        'program_anasayfa': veri #Genel temlateye logo ismi ile döndürdük
    }

def logolar_anasayfa(request):
    veri =  Logos.objects.all()
    return {
        'logos': veri #Genel temlateye logo ismi ile döndürdük
    }

def projeanasayfa(request):
    veri =  Proje_anasayfa.objects.all()
    return {
        'projeanasayfa': veri #Genel temlateye logo ismi ile döndürdük
    }
def hakkımızda(request):
    veri =  Hakkimizda.objects.all()
    return {
        'hakkımızda': veri #Genel temlateye logo ismi ile döndürdük
    }




def ayar(request):
    veri =  Settings.objects.all()
    return {
        'ayar': veri #Genel temlateye logo ismi ile döndürdük
    }

def adres(request):
    veri =  Adres.objects.all()
    return {
        'adres': veri #Genel temlateye logo ismi ile döndürdük
    }

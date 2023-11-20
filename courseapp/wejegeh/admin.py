from django.contrib import admin
from .models import Renk,Program_Anasayfa,Program_Etkinlik,Logos,Porogram_E_Foto
from .models import Hakkimizda
from .models import Proje_anasayfa,Proje_slide,Proje_icerik,Proje_Etkinlik,Settings,Photo,Slide_index
from .models import Yıl,Tür,Alan,Adres,Bölüm
from .models import Ev_Yayıncılık,Slide,Contents,Anasayfa,Yazi,Takvim

admin.site.register(Yazi)
class Ev_YayıncılıkAdmin(admin.ModelAdmin):
    list_display = ('baslik_tr', 'name')
    list_filter = ('ust_kategori__name',) # Filtreleme seçenekleri ekler
admin.site.register(Ev_Yayıncılık, Ev_YayıncılıkAdmin)   

class AnasayfaAdmin(admin.ModelAdmin):
    list_display = ('baslik_tr', 'name')
    list_filter = ('name',) # Filtreleme seçenekleri ekler
admin.site.register(Anasayfa, AnasayfaAdmin)   

admin.site.register(Takvim)
admin.site.register(Slide)
admin.site.register(Contents)



admin.site.register(Adres)
admin.site.register(Photo)
admin.site.register(Slide_index)
admin.site.register(Bölüm)
admin.site.register(Settings)


admin.site.register(Proje_anasayfa)
admin.site.register(Proje_slide)
admin.site.register(Proje_icerik)
admin.site.register(Proje_Etkinlik)


admin.site.register(Program_Etkinlik)
admin.site.register(Porogram_E_Foto)
admin.site.register(Program_Anasayfa)
admin.site.register(Renk)
admin.site.register(Hakkimizda)

admin.site.register(Logos)
admin.site.register(Yıl)
admin.site.register(Tür)
admin.site.register(Alan)


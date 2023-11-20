from django.db import models
import datetime
from django.utils.text import slugify #slugify (java-kursu) import ettik


class Slide_index(models.Model):
    tarih=models.DateField(verbose_name="Tarih",blank=True)
    resim = models.ImageField(upload_to='index/slide')
    redirect_url = models.URLField(blank=True)


class Yıl(models.Model):
    yıl = models.IntegerField()
    def __str__(self):
        return str(self.yıl)
  
class Tür(models.Model):
    tür_tr = models.CharField(max_length=50,blank=True)
    tür_ku = models.CharField(max_length=50,blank=True)
    tür_en = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.tür_tr
class Alan(models.Model):
    alan_tr = models.CharField(max_length=50,blank=True)
    alan_ku = models.CharField(max_length=50,blank=True)
    alan_en = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.alan_tr
class Bölüm(models.Model):
    bölüm_tr = models.CharField(max_length=50,blank=True)
    bölüm_ku = models.CharField(max_length=50,blank=True)
    bölüm_en = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.bölüm_tr
    


class Renk(models.Model):
    renk_adi = models.TextField(blank=True)
    renk_code=models.TextField(blank=True)
    def __str__(self):
        return self.renk_adi


class Program_Anasayfa(models.Model):
    renk = models.ForeignKey(Renk, on_delete=models.CASCADE)
    baslik_tr = models.CharField(max_length=100,blank=True)
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)
    aciklama_tr = models.TextField(blank=True)
    aciklama_ku = models.TextField(blank=True)
    aciklama_en = models.TextField(blank=True)
    
    foto_tr = models.ImageField(upload_to='program/fotoanasayfa',blank=True)
    foto_ku = models.ImageField(upload_to='program/fotoanasayfa',blank=True)
    foto_en = models.ImageField(upload_to='program/fotoanasayfa',blank=True)
    slug_tr = models.SlugField(default="", null=False, blank=True)
    slug_ku = models.SlugField(default="", null=False, blank=True)
    slug_en = models.SlugField(default="", null=False, blank=True)
    def __str__(self):
        return self.baslik_tr
    def save(self, *args, **kwargs):
        if not self.slug_tr and self.baslik_tr:
            self.slug_tr = slugify(self.baslik_tr)
        if not self.slug_ku and self.baslik_ku:
            self.slug_ku = slugify(self.baslik_ku)
        if not self.slug_en and self.baslik_en:
            self.slug_en = slugify(self.baslik_en)
        super().save(*args, **kwargs)

class Porogram_E_Foto(models.Model):
    
    foto_name = models.CharField(max_length=100,blank=True)
    foto = models.ImageField(upload_to='program_etkinlik')
    redirect_url = models.URLField(blank=True)

    def __str__(self):
        return self.foto_name


class Program_Etkinlik(models.Model):
    tarih=models.DateField(verbose_name="Tarih",blank=True)
    Ust_kategori = models.ForeignKey(Program_Anasayfa, on_delete=models.CASCADE,related_name='program_etkinlikler')
    Ustkategori_foto=models.ImageField(upload_to='program/fotoanasayfa')#zorunlu
    etkinlik_fotoları = models.ManyToManyField(Porogram_E_Foto,blank=True)

    baslik_tr = models.CharField(max_length=100)#zorunlu
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)
    
    yazar_tr = models.CharField(max_length=100,blank=True)
    yazar_ku = models.CharField(max_length=100,blank=True)
    yazar_en = models.CharField(max_length=100,blank=True)
    
    metin_tr = models.TextField(blank=True)
    metin_ku = models.TextField(blank=True)
    metin_en = models.TextField(blank=True)
    
    tür=models.ForeignKey(Tür,on_delete=models.CASCADE,blank=True, null=True,related_name='program_etkinlikler')
    alan=models.ForeignKey(Alan,on_delete=models.CASCADE,blank=True, null=True,related_name='program_etkinlikler')
    
    bölüm_alanı=models.ForeignKey(Bölüm,on_delete=models.CASCADE,blank=True, null=True,related_name='program_etkinlikler')
    
    
    
    slug_tr = models.SlugField(default="", null=False, blank=True)
    slug_ku = models.SlugField(default="", null=False, blank=True)
    slug_en = models.SlugField(default="", null=False, blank=True)
    
    arşiv_seçkisi=models.BooleanField(blank=True)
    genel_active=models.BooleanField(blank=True)
    active_tr=models.BooleanField(blank=True)
    active_ku=models.BooleanField(blank=True)
    active_en=models.BooleanField(blank=True)
    active_anasayfa=models.BooleanField(blank=True)
    active_takvim=models.BooleanField(blank=True)
    arşiv_seçkisi=models.BooleanField(blank=True)
    takvim_renk=models.ForeignKey(Renk, on_delete=models.CASCADE,blank=True, null=True,related_name='program_etkinlikler')
    def __str__(self):
        return self.baslik_tr
    def save(self, *args, **kwargs):
        if not self.slug_tr and self.baslik_tr:
            self.slug_tr = slugify(self.baslik_tr)
        if not self.slug_ku and self.baslik_ku:
            self.slug_ku = slugify(self.baslik_ku)
        if not self.slug_en and self.baslik_en:
            self.slug_en = slugify(self.baslik_en)
        super().save(*args, **kwargs)


class Logos(models.Model):
    logo_name = models.CharField(max_length=100,blank=True)
    logo = models.ImageField(upload_to='logos/')
    colored_image = models.ImageField(upload_to='colored_images/')
    redirect_url = models.URLField()
    def __str__(self):
        return self.logo_name



class Proje_anasayfa(models.Model):
    baslik_tr = models.CharField(max_length=100,blank=True)
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)

    aciklama_tr = models.TextField(blank=True)
    aciklama_ku = models.TextField(blank=True)
    aciklama_en = models.TextField(blank=True)

    foto_tr = models.ImageField(upload_to='proje/fotoanasayfa',blank=True)
    foto_ku = models.ImageField(upload_to='proje/fotoanasayfa',blank=True)
    foto_en = models.ImageField(upload_to='proje/fotoanasayfa',blank=True)

    slug_tr = models.SlugField(default="", null=False, blank=True)
    slug_ku = models.SlugField(default="", null=False, blank=True)
    slug_en = models.SlugField(default="", null=False, blank=True)

    def __str__(self):
        return self.baslik_tr

    def save(self, *args, **kwargs):
        if not self.slug_tr and self.baslik_tr:
            self.slug_tr = slugify(self.baslik_tr)
        if not self.slug_ku and self.baslik_ku:
            self.slug_ku = slugify(self.baslik_ku)
        if not self.slug_en and self.baslik_en:
            self.slug_en = slugify(self.baslik_en)
        super().save(*args, **kwargs)

class Proje_icerik(models.Model):
    paragraf_adi = models.CharField(max_length=100,blank=True)
    metin_tr = models.TextField(blank=True)
    metin_ku = models.TextField(blank=True)
    metin_en = models.TextField(blank=True)
    foto = models.ImageField(upload_to='proje/foto')
    def __str__(self):
        return self.paragraf_adi

class Proje_slide(models.Model):
    slide_name = models.CharField(max_length=100,blank=True)
    foto=models.ImageField(upload_to='proje/slide')#zorunlu
    def __str__(self):
        return self.slide_name

class Proje_Etkinlik(models.Model):
    tarih=models.DateField(verbose_name="Tarih",blank=True)
    Ust_kategori = models.ForeignKey(Proje_anasayfa, on_delete=models.CASCADE,related_name='proje_etkinlikler')
    Ustkategori_foto=models.ImageField(upload_to='program/fotoanasayfa')#zorunlu
    Ustkategori_renk=models.ForeignKey(Renk, on_delete=models.CASCADE,related_name='projeüst_etkinlikler')#zorunlu
    foto=models.ImageField(upload_to='program/foto',blank=True)#zorunlu
    baslik_tr = models.CharField(max_length=100)#zorunlu
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)
    proje_içerik = models.ManyToManyField(Proje_icerik,blank=True)
    proje_slides = models.ManyToManyField(Proje_slide,blank=True)
    
    tür=models.ForeignKey(Tür,on_delete=models.CASCADE,blank=True,null=True,related_name='proje_etkinlikler')
    alan=models.ForeignKey(Alan,on_delete=models.CASCADE,blank=True,null=True,related_name='proje_etkinlikler')
    bölüm_alanı=models.ForeignKey(Bölüm,on_delete=models.CASCADE,blank=True, null=True,related_name='proje_etkinlikler')
    

    slug_tr = models.SlugField(default="", null=False, blank=True)
    slug_ku = models.SlugField(default="", null=False, blank=True)
    slug_en = models.SlugField(default="", null=False, blank=True)

    arşiv_seçkisi=models.BooleanField(blank=True)
    slide_active=models.BooleanField(blank=True)
    genel_active=models.BooleanField(blank=True)
    active_tr=models.BooleanField(blank=True)
    active_ku=models.BooleanField(blank=True)
    active_en=models.BooleanField(blank=True)
    active_anasayfa=models.BooleanField(blank=True)
    active_takvim=models.BooleanField(blank=True)
    takvim_renk=models.ForeignKey(Renk, on_delete=models.CASCADE,blank=True, null=True,related_name='proje_etkinlikler')
    def __str__(self):
        return self.baslik_tr
    def save(self, *args, **kwargs):
        if not self.slug_tr and self.baslik_tr:
            self.slug_tr = slugify(self.baslik_tr)
        if not self.slug_ku and self.baslik_ku:
            self.slug_ku = slugify(self.baslik_ku)
        if not self.slug_en and self.baslik_en:
            self.slug_en = slugify(self.baslik_en)
        super().save(*args, **kwargs)


class Photo(models.Model):
    url = models.ImageField(upload_to='photos/')  # Django'nun ImageField'ını kullanarak fotoğrafı yüklemek için
    alt_text = models.CharField(max_length=255, help_text="Fotoğraf için alternatif metin")
    caption = models.TextField(blank=True, help_text="Fotoğraf altındaki açıklama veya başlık")

    def __str__(self):
        return self.alt_text


class Hakkimizda(models.Model):
    foto=models.ImageField(upload_to='hakkımızda')#zorunlu
    baslik_tr = models.CharField(max_length=100,blank=True)
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)
    metin_tr = models.TextField(blank=True)
    metin_ku = models.TextField(blank=True)
    metin_en = models.TextField(blank=True)
    def __str__(self):
        return self.baslik_tr




class Yazi(models.Model):
    name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name

class Settings(models.Model):
    name = models.CharField(max_length=100,blank=True)
    favicon=models.ImageField(upload_to='genel/favicon',blank=True)#zorunlu
    logo=models.ImageField(upload_to='genel/logo',blank=True)#zorunlu
    yazi_tipi =  models.ForeignKey(Yazi, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Adres(models.Model):
    name=models.CharField( max_length=50)
    foto=models.ImageField(upload_to='adres/foto',blank=True)#zorunlu
    adres_tr = models.TextField(blank=True)
    adres_ku = models.TextField(blank=True)
    adres_en = models.TextField(blank=True)
    numara=models.CharField( max_length=50, blank=True)
    e_mail=models.EmailField(blank=True)
    def __str__(self):
        return self.name



class Anasayfa(models.Model):
    BIRIM_CHOICES = [
        ('Ev', 'Ev'),
        ('Yayıncılık', 'Yayıncılık'),
        # Diğer birimler buraya eklenebilir
    ]
    name = models.CharField(max_length=50, choices=BIRIM_CHOICES)

    baslik_tr = models.CharField(max_length=100,blank=True)
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)

    foto_tr = models.ImageField(upload_to='proje/fotoanasayfa',blank=True)
    foto_ku = models.ImageField(upload_to='proje/fotoanasayfa',blank=True)
    foto_en = models.ImageField(upload_to='proje/fotoanasayfa',blank=True)
    
    slug_tr = models.SlugField(default="", null=False, blank=True)
    slug_ku = models.SlugField(default="", null=False, blank=True)
    slug_en = models.SlugField(default="", null=False, blank=True)

    def __str__(self):
        return self.baslik_tr

    def save(self, *args, **kwargs):
        if not self.slug_tr and self.baslik_tr:
            self.slug_tr = slugify(self.baslik_tr)
        if not self.slug_ku and self.baslik_ku:
            self.slug_ku = slugify(self.baslik_ku)
        if not self.slug_en and self.baslik_en:
            self.slug_en = slugify(self.baslik_en)
        super().save(*args, **kwargs)

class Contents(models.Model):
    paragraf_adi = models.CharField(max_length=100,blank=True)
    metin_tr = models.TextField(blank=True)
    metin_ku = models.TextField(blank=True)
    metin_en = models.TextField(blank=True)
    foto = models.ImageField(upload_to='ev_yayıncılık/foto')
    def __str__(self):
        return self.paragraf_adi

class Slide(models.Model):
    slide_name = models.CharField(max_length=100,blank=True)
    foto=models.ImageField(upload_to='ev_yayıncılık/slide')#zorunlu
    def __str__(self):
        return self.slide_name

class Ev_Yayıncılık(models.Model):
    BIRIM_CHOICES = [
        ('Ev', 'Ev'),
        ('Yayıncılık', 'Yayıncılık'),
        # Diğer birimler buraya eklenebilir 
    ]
    name = models.CharField(max_length=50, choices=BIRIM_CHOICES)
    tarih=models.DateField(verbose_name="Tarih",blank=True)
    ust_kategori = models.ForeignKey(Anasayfa, on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='ev_yayıncılık/foto',blank=True)#zorunlu
    baslik_tr = models.CharField(max_length=100)#zorunlu
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)
    içerik = models.ManyToManyField(Contents,blank=True)
    slides = models.ManyToManyField(Slide,blank=True)
    
    slug_tr = models.SlugField(default="", null=False, blank=True)
    slug_ku = models.SlugField(default="", null=False, blank=True)
    slug_en = models.SlugField(default="", null=False, blank=True)

    genel_active=models.BooleanField(blank=True)
    active_tr=models.BooleanField(blank=True)
    active_ku=models.BooleanField(blank=True)
    active_en=models.BooleanField(blank=True)
    def __str__(self):
        return self.baslik_tr
    def save(self, *args, **kwargs):
        if not self.slug_tr and self.baslik_tr:
            self.slug_tr = slugify(self.baslik_tr)
        if not self.slug_ku and self.baslik_ku:
            self.slug_ku = slugify(self.baslik_ku)
        if not self.slug_en and self.baslik_en:
            self.slug_en = slugify(self.baslik_en)
        super().save(*args, **kwargs)


class Takvim(models.Model):
    baslik_tr = models.CharField(max_length=100,blank=True)
    baslik_ku = models.CharField(max_length=100,blank=True)
    baslik_en = models.CharField(max_length=100,blank=True)
    
    metin_tr = models.TextField(blank=True)
    metin_ku = models.TextField(blank=True)
    metin_en = models.TextField(blank=True)
    
    foto_tr = models.ImageField(upload_to='takvim/tr')
    foto_ku = models.ImageField(upload_to='takvim/kr')
    foto_en = models.ImageField(upload_to='takvim/en')
    def __str__(self):
        return self.baslik_tr
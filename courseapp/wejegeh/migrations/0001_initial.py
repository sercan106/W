# Generated by Django 4.1.3 on 2023-10-30 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('foto', models.ImageField(blank=True, upload_to='adres/foto')),
                ('adres_tr', models.TextField(blank=True)),
                ('adres_ku', models.TextField(blank=True)),
                ('adres_en', models.TextField(blank=True)),
                ('numara', models.CharField(blank=True, max_length=50)),
                ('e_mail', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Alan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alan_tr', models.CharField(blank=True, max_length=50)),
                ('alan_ku', models.CharField(blank=True, max_length=50)),
                ('alan_en', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Anasayfa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Ev', 'Ev'), ('Yayıncılık', 'Yayıncılık')], max_length=50)),
                ('baslik_tr', models.CharField(blank=True, max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('foto_tr', models.ImageField(blank=True, upload_to='proje/fotoanasayfa')),
                ('foto_ku', models.ImageField(blank=True, upload_to='proje/fotoanasayfa')),
                ('foto_en', models.ImageField(blank=True, upload_to='proje/fotoanasayfa')),
                ('slug_tr', models.SlugField(blank=True, default='')),
                ('slug_ku', models.SlugField(blank=True, default='')),
                ('slug_en', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Bölüm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bölüm_tr', models.CharField(blank=True, max_length=50)),
                ('bölüm_ku', models.CharField(blank=True, max_length=50)),
                ('bölüm_en', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraf_adi', models.CharField(blank=True, max_length=100)),
                ('metin_tr', models.TextField(blank=True)),
                ('metin_ku', models.TextField(blank=True)),
                ('metin_en', models.TextField(blank=True)),
                ('foto', models.ImageField(upload_to='ev_yayıncılık/foto')),
            ],
        ),
        migrations.CreateModel(
            name='Hakkimizda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='hakkımızda')),
                ('baslik_tr', models.CharField(blank=True, max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('metin_tr', models.TextField(blank=True)),
                ('metin_ku', models.TextField(blank=True)),
                ('metin_en', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_name', models.CharField(blank=True, max_length=100)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('colored_image', models.ImageField(upload_to='colored_images/')),
                ('redirect_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='photos/')),
                ('alt_text', models.CharField(help_text='Fotoğraf için alternatif metin', max_length=255)),
                ('caption', models.TextField(blank=True, help_text='Fotoğraf altındaki açıklama veya başlık')),
            ],
        ),
        migrations.CreateModel(
            name='Porogram_E_Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_name', models.CharField(blank=True, max_length=100)),
                ('foto', models.ImageField(upload_to='program_etkinlik')),
                ('redirect_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program_Anasayfa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik_tr', models.CharField(blank=True, max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('aciklama_tr', models.TextField(blank=True)),
                ('aciklama_ku', models.TextField(blank=True)),
                ('aciklama_en', models.TextField(blank=True)),
                ('foto_tr', models.ImageField(blank=True, upload_to='program/fotoanasayfa')),
                ('foto_ku', models.ImageField(blank=True, upload_to='program/fotoanasayfa')),
                ('foto_en', models.ImageField(blank=True, upload_to='program/fotoanasayfa')),
                ('slug_tr', models.SlugField(blank=True, default='')),
                ('slug_ku', models.SlugField(blank=True, default='')),
                ('slug_en', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Proje_anasayfa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik_tr', models.CharField(blank=True, max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('aciklama_tr', models.TextField(blank=True)),
                ('aciklama_ku', models.TextField(blank=True)),
                ('aciklama_en', models.TextField(blank=True)),
                ('foto_tr', models.ImageField(blank=True, upload_to='proje/fotoanasayfa')),
                ('foto_ku', models.ImageField(blank=True, upload_to='proje/fotoanasayfa')),
                ('foto_en', models.ImageField(blank=True, upload_to='proje/fotoanasayfa')),
                ('slug_tr', models.SlugField(blank=True, default='')),
                ('slug_ku', models.SlugField(blank=True, default='')),
                ('slug_en', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Proje_icerik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraf_adi', models.CharField(blank=True, max_length=100)),
                ('metin_tr', models.TextField(blank=True)),
                ('metin_ku', models.TextField(blank=True)),
                ('metin_en', models.TextField(blank=True)),
                ('foto', models.ImageField(upload_to='proje/foto')),
            ],
        ),
        migrations.CreateModel(
            name='Proje_slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_name', models.CharField(blank=True, max_length=100)),
                ('foto', models.ImageField(upload_to='proje/slide')),
            ],
        ),
        migrations.CreateModel(
            name='Renk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renk_adi', models.TextField(blank=True)),
                ('renk_code', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_name', models.CharField(blank=True, max_length=100)),
                ('foto', models.ImageField(upload_to='ev_yayıncılık/slide')),
            ],
        ),
        migrations.CreateModel(
            name='Slide_index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField(blank=True, verbose_name='Tarih')),
                ('resim', models.ImageField(upload_to='index/slide')),
            ],
        ),
        migrations.CreateModel(
            name='Tür',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tür_tr', models.CharField(blank=True, max_length=50)),
                ('tür_ku', models.CharField(blank=True, max_length=50)),
                ('tür_en', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Yazi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Yıl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yıl', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('favicon', models.ImageField(blank=True, upload_to='genel/favicon')),
                ('logo', models.ImageField(blank=True, upload_to='genel/logo')),
                ('yazi_tipi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wejegeh.yazi')),
            ],
        ),
        migrations.CreateModel(
            name='Proje_Etkinlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField(blank=True, verbose_name='Tarih')),
                ('Ustkategori_foto', models.ImageField(upload_to='program/fotoanasayfa')),
                ('foto', models.ImageField(blank=True, upload_to='program/foto')),
                ('baslik_tr', models.CharField(max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('slug_tr', models.SlugField(blank=True, default='')),
                ('slug_ku', models.SlugField(blank=True, default='')),
                ('slug_en', models.SlugField(blank=True, default='')),
                ('arşiv_seçkisi', models.BooleanField(blank=True)),
                ('slide_active', models.BooleanField(blank=True)),
                ('genel_active', models.BooleanField(blank=True)),
                ('active_tr', models.BooleanField(blank=True)),
                ('active_ku', models.BooleanField(blank=True)),
                ('active_en', models.BooleanField(blank=True)),
                ('active_anasayfa', models.BooleanField(blank=True)),
                ('active_takvim', models.BooleanField(blank=True)),
                ('Ust_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proje_etkinlikler', to='wejegeh.proje_anasayfa')),
                ('Ustkategori_renk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projeüst_etkinlikler', to='wejegeh.renk')),
                ('alan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proje_etkinlikler', to='wejegeh.alan')),
                ('bölüm_alanı', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proje_etkinlikler', to='wejegeh.bölüm')),
                ('proje_içerik', models.ManyToManyField(blank=True, to='wejegeh.proje_icerik')),
                ('proje_slides', models.ManyToManyField(blank=True, to='wejegeh.proje_slide')),
                ('takvim_renk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proje_etkinlikler', to='wejegeh.renk')),
                ('tür', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proje_etkinlikler', to='wejegeh.tür')),
            ],
        ),
        migrations.CreateModel(
            name='Program_Etkinlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarih', models.DateField(blank=True, verbose_name='Tarih')),
                ('Ustkategori_foto', models.ImageField(upload_to='program/fotoanasayfa')),
                ('baslik_tr', models.CharField(max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('yazar_tr', models.CharField(blank=True, max_length=100)),
                ('yazar_ku', models.CharField(blank=True, max_length=100)),
                ('yazar_en', models.CharField(blank=True, max_length=100)),
                ('metin_tr', models.TextField(blank=True)),
                ('metin_ku', models.TextField(blank=True)),
                ('metin_en', models.TextField(blank=True)),
                ('slug_tr', models.SlugField(blank=True, default='')),
                ('slug_ku', models.SlugField(blank=True, default='')),
                ('slug_en', models.SlugField(blank=True, default='')),
                ('genel_active', models.BooleanField(blank=True)),
                ('active_tr', models.BooleanField(blank=True)),
                ('active_ku', models.BooleanField(blank=True)),
                ('active_en', models.BooleanField(blank=True)),
                ('active_anasayfa', models.BooleanField(blank=True)),
                ('active_takvim', models.BooleanField(blank=True)),
                ('arşiv_seçkisi', models.BooleanField(blank=True)),
                ('Ust_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_etkinlikler', to='wejegeh.program_anasayfa')),
                ('alan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_etkinlikler', to='wejegeh.alan')),
                ('bölüm_alanı', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_etkinlikler', to='wejegeh.bölüm')),
                ('etkinlik_fotoları', models.ManyToManyField(blank=True, to='wejegeh.porogram_e_foto')),
                ('takvim_renk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_etkinlikler', to='wejegeh.renk')),
                ('tür', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_etkinlikler', to='wejegeh.tür')),
            ],
        ),
        migrations.AddField(
            model_name='program_anasayfa',
            name='renk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wejegeh.renk'),
        ),
        migrations.CreateModel(
            name='Ev_Yayıncılık',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Ev', 'Ev'), ('Yayıncılık', 'Yayıncılık')], max_length=50)),
                ('tarih', models.DateField(blank=True, verbose_name='Tarih')),
                ('foto', models.ImageField(blank=True, upload_to='ev_yayıncılık/foto')),
                ('baslik_tr', models.CharField(max_length=100)),
                ('baslik_ku', models.CharField(blank=True, max_length=100)),
                ('baslik_en', models.CharField(blank=True, max_length=100)),
                ('slug_tr', models.SlugField(blank=True, default='')),
                ('slug_ku', models.SlugField(blank=True, default='')),
                ('slug_en', models.SlugField(blank=True, default='')),
                ('genel_active', models.BooleanField(blank=True)),
                ('active_tr', models.BooleanField(blank=True)),
                ('active_ku', models.BooleanField(blank=True)),
                ('active_en', models.BooleanField(blank=True)),
                ('içerik', models.ManyToManyField(blank=True, to='wejegeh.contents')),
                ('slides', models.ManyToManyField(blank=True, to='wejegeh.slide')),
                ('ust_kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wejegeh.anasayfa')),
            ],
        ),
    ]

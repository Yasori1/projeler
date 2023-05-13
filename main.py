print("Emeklilik Hesaplama Programı:")
from datetime import date

def yil_hesapla(tarih):
    bugun = date.today()
    return bugun.year - tarih.year - ((bugun.month, bugun.day) < (tarih.month, tarih.day))

def emeklilik_hesapla(isim, dogum_tarihi, sigorta_baslangic_tarihi, gun):
    yas = yil_hesapla(dogum_tarihi)
    sigortalilik_suresi = yil_hesapla(sigorta_baslangic_tarihi)
    if gun < 9000:
        kalan_gun1 = 9000 - gun
        return "{}, Emekli olamazsınız. Gününüz dolmamıştır. Emekliliğe {} gün kalmıştır.".format(isim, kalan_gun1)
    elif yas >= 15 and gun >= 10000:
        return "{}, EYT ile Emeklisiniz.".format(isim)
    elif yas >= 20 and gun >= 9000:
        return "{}, Yaşınız ve Gününüz dolmuştur. Emekli olabilirsiniz.".format(isim)
    else:
        kalan_gun2 = (15 - sigortalilik_suresi) * 365 + (10000 - gun)
        return "{}, EYT'ye takılı kaldınız. Gün sayısınız az .Emekliliğe {} gün kalmıştır.".format(isim, kalan_gun2)

isim = input("Lütfen İsminizi Girin: ")

hitap = input("Lütfen Hitap Şeklinizi Girin (Bey/Hanım): ")

dogum_ay_adi = input("Lütfen Doğduğunuz Ayın Adını Girin (Ocak, Şubat, ...): ")

dogum_yili = int(input("Lütfen Doğum Yılınızı Girin: "))

dogum_gunu = int(input("Lütfen Doğum Gününüzü Girin: "))

def ay_no(ad):
 aylar = {
    "Ocak": 1,
    "Şubat": 2,
    "Mart": 3,
    "Nisan": 4,
    "Mayıs": 5,
    "Haziran": 6,
    "Temmuz": 7,
    "Ağustos": 8,
    "Eylül": 9,
    "Ekim": 10,
    "Kasım": 11,
    "Aralık": 12
}
 if ad in aylar:
     return aylar[ad]
 else:
     print("Hata: Geçersiz ay adı.")


sigorta_baslangic_ayi=ay_no(input("Lütfen Giriş Yaptığınız Ayın Adını Girin(Ocak,Şubat ...):"))

sigorta_baslangic_yili=int(input("Lütfen Sigorta Başlangıç Yılınızı Girin:"))
def gunler(sayi):
    gunler={
        "Pazartesi":1,
        "Salı":2,
        "Çarşamba":3,
        "Perşembe":4,
        "Cuma":5,
        "Cumartesi":6,
        "Pazar":7,
    }
    if sayi in gunler:
        return gunler[sayi]
    else:
        print("Hata: Geçersiz gün adı.")


sigorta_baslangic_gunu = gunler(str(input("Lütfen Sigorta Başlangıç Gününüzü Girin:")))

gun=int(input("Lütfen Toplam Prim Gün Sayısını Girin:"))

dogum_ayi = ay_no(dogum_ay_adi)
print("Doğum ayı:", dogum_ayi)
sigorta_baslangic_ayi = ay_no(sigorta_baslangic_ayi)
print("Sigorta başlangıç ayı:", sigorta_baslangic_ayi)

dogum_tarihi = date(dogum_yili, dogum_ayi, dogum_gunu)
sigorta_baslangic_tarihi = date(sigorta_baslangic_yili, sigorta_baslangic_ayi, sigorta_baslangic_gunu)
sonuc = emeklilik_hesapla(isim + " " + hitap,dogum_tarihi,sigorta_baslangic_tarihi,gun)

print(sonuc)


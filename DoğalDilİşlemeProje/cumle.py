import re

def temizle(metin):
    # Parantez içindeki metinleri bulmak için bir regex deseni oluşturuyoruz
    parantez_deseni = re.compile(r'\([^()]*\)')  # Parantezler arasındaki herhangi bir şeyi bul

    # Parantez içindeki metinleri çıkarıyoruz
    temizlenmis_metin = re.sub(parantez_deseni, '', metin)

    # Ardışık boşlukları tek bir boşlukla değiştiriyoruz ve metnin başındaki ve sonundaki boşlukları kaldırıyoruz
    temizlenmis_metin = ' '.join(temizlenmis_metin.split())

    return temizlenmis_metin


import get_cumles
import get_deyimler
def siradaki_satiri_oku(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='UTF-8') as dosya:
        for satir in dosya:
            yield satir.strip()

dosya_yolu = 'Deyimler.txt'  # Okunacak dosyanın yolu
satir_okuyucu = siradaki_satiri_oku(dosya_yolu)

# Her döngüde bir sonraki satırı okuyarak işlem yapma
for i in range(10979):
    try:
        siradaki_satir = next(satir_okuyucu)
        dosya=open("Deyim_cümleleri.txt","a",encoding="UTF-8")
        dosya.write(siradaki_satir+" deyimiyle ilgili cümleler: \n")
        dosya.close()
        dosyac=open("output.conll","a",encoding="UTF-8")
        dosyac.write(siradaki_satir+" deyimiyle ilgili cümlelerin conll formatı")
        dosyac.close
        get_cumles.kelime_bul(siradaki_satir)
        dosya=open("Deyim_cümleleri.txt","a",encoding="UTF-8")
        dosya.write("\n\n")
        dosya.close()
    except StopIteration:
        print("Dosya sonuna ulaşıldı.")
        break
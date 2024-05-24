def cumle_kontrol( aranan_cumle):
    try:
        # Dosyayı oku
        with open("Deyim_cümleleri.txt", "r",encoding="UTF-8") as dosya:
            icerik = dosya.read()
        
            # Aranan cümleyi kontrol et
            if aranan_cumle.lower() in icerik.lower():
                return False
                
            else:
                return True
    except FileNotFoundError:
        print("Dosya bulunamadı.")


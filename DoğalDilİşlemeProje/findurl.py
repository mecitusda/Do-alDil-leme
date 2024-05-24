from googlesearch import search
import time
import random

def google_arama_url(arama_terimi, sayfa_sayısı=100):
    url_listesi = []
    # Google arama sonuçlarını al
    for url in search(arama_terimi, num=sayfa_sayısı, stop=sayfa_sayısı, pause=2):
        url_listesi.append(url)

    return url_listesi



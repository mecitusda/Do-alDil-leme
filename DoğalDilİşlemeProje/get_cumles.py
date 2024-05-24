import requests
from bs4 import BeautifulSoup
import findurl
import time
import dosyaoku
import conll



dosya=open("Deyim_cümleleri.txt","w")
dosya.close()
dosyac=open("output.conll","w")
dosyac.close()

from fake_useragent import UserAgent

def kelime_bul(search_word):
    
    urls=findurl.google_arama_url('"'+search_word+'"')
    
    counter=1

    for url in urls:
        
        ua = UserAgent()
        headers = {
        "User-Agent": ua.random
        }
        response = requests.get(url,headers)
        time.sleep(1)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            metin = soup.get_text()
            metin=metin.split(".")
            print("cümleler bulunuyor.")
            for i in metin:
                a=i.split("?")
                if len(a)>1:
                    for c in a: 
                        if(search_word in c.lower()):
                                j=c.split("  ")
                                if len(j)>1:
                                    continue
                                else:
                                    if c =="":
                                        continue
                                    else:
                                        if  dosyaoku.cumle_kontrol(((c.strip()).replace("\n",""))):
                                            
                                            dosya=open("Deyim_cümleleri.txt","a",encoding="UTF-8")
                                            sonhal=((c.strip()).replace("\n","")+".\n").split('"')
                                            if(len(sonhal)==1):
                                                dosya.write(str(counter)+"."+sonhal[0])
                                                dosya.close()
                                                conll.translate_conll(sonhal[0])
                                                counter+=1
                                            else:   
                                                for b in sonhal:
                                                
                                                    if(len(b)>4):
                                                        
                                                        dosya.write(str(counter)+"."+b)
                                                        dosya.close()
                                                        conll.translate_conll(b)
                                                        counter+=1
                                        
                else:
                
                    if(search_word in i.lower()):
                           k=i.split("  ")
                           if(len(k)>1):
                                continue
                           else:
                            if i=="":
                                continue
                            else:
                                if dosyaoku.cumle_kontrol(((i.strip()).replace("\n",""))):
                                    dosya=open("Deyim_cümleleri.txt","a",encoding="UTF-8")
                                    sonhal=((i.strip()).replace("\n","")+".\n").split('"')
                                    if(len(sonhal)==1):
                                                dosya.write(str(counter)+"."+sonhal[0])
                                                dosya.close()
                                                conll.translate_conll(str(counter)+"."+sonhal[0])
                                                counter+=1
                                    else:   
                                        for b in sonhal:
                                                
                                            if(len(b)>4):
                                                dosya.write(str(counter)+"."+b)
                                                dosya.close()
                                                conll.translate_conll(str(counter)+"."+b)
                                                counter+=1
                if counter==101:
                    exit()
    
        else:
            print("Web sitesine ulaşılamadı.")
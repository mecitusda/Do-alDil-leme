import requests
import xml.etree.ElementTree as ET
import cumle
dosya=open("Deyimler.txt","w",encoding="UTF-8")
dosya.close()
url = "https://www.netdata.com/XML/a4b2d476"
response = requests.get(url)

if response.status_code == 200:
    root = ET.fromstring(response.content)
    for element in root.iter():
        if(element.tag == "dc_Deyim"):
            cümle=element.text
            temizlenmiş_cümle=cumle.temizle(cümle)
            if(temizlenmiş_cümle.__contains__("?")):
                temizlenmiş_cümle=temizlenmiş_cümle.replace("?","")
            dosya=open("Deyimler.txt","a",encoding="UTF-8")
            dosya.write(temizlenmiş_cümle+"\n")
            dosya.close()
    print("Deyimler Alındı.")        
else:
    print("İstek başarısız oldu:", response.status_code)

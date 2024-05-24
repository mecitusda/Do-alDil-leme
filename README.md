# Doğal dil işleme proje resim

## Türkçedeki bütün deyimleri bir xml dosyasından çekiyorum
### https://www.netdata.com/XML/a4b2d476
![resim1](https://github.com/mecitusda/DogalDilisleme/assets/92247286/a1f1451d-eda9-4039-abc2-7738d857471d)

## Her bir deyim için örnek cümleleri bir .txt dosyasına kaydediyorum.

![resim4](https://github.com/mecitusda/DogalDilisleme/assets/92247286/91c20ea6-ba08-4ed1-9fdb-5e68ce582be5)

## Her bir bulunan örnek cümleyi conll formatına çevirip .conll formatında bir dosyaya kaydediyorum.

![resim3](https://github.com/mecitusda/DogalDilisleme/assets/92247286/f8e6289b-410f-4848-9af1-298625706607)

## Burada deyimleri üsttede belirttiğim gibi xml dosyasından çekiyorum.

![deyimler](https://github.com/mecitusda/DogalDilisleme/assets/92247286/9acac1cb-f861-4188-a5f9-b45d24392e37)
## Burada deyimleri dosyadan tek tek okuyorum.

![dosyaoku](https://github.com/mecitusda/DogalDilisleme/assets/92247286/f642a164-a4d4-4022-8f4c-3792fc3cbf5f)


## Burada okunan deyimleri googleda arama yapıp deyimleri içeren web sitelerinin url'lerini toplayıp geriye döndürüyorum.

![dosyaokus](https://github.com/mecitusda/DogalDilisleme/assets/92247286/bbf7b391-cb2b-4dd5-8eda-f3c219328e6f)
## Burada metin içerisindeki html parsin işleminden kaynaklanabilen gereksiz karakterleri temizliyorum.

![cumle](https://github.com/mecitusda/DogalDilisleme/assets/92247286/66f405cf-4e47-4e13-a08c-2c610c6bda51)

## Burada geri döndürülen url'lerden döngü yardımıyla sayfa html bilgisini çekiyorum ve belirli algoritmayla içerisindeki aradığım cümleleri çekip dosyaya yazıyorum.

![getcumles1](https://github.com/mecitusda/DogalDilisleme/assets/92247286/97ad9c6f-577a-4c45-af76-6c13756b9def)
![getcumles2](https://github.com/mecitusda/DogalDilisleme/assets/92247286/1878b4bf-060d-454e-97c5-624f214c994c)

## Burası ise ana fonksiyonum.
### - İlk olarak deyimleri yazdığım fonksiyon ile txt dosyasına yazdırıyorum.
### - Deyim sayısı kadar döngü kurarak her deyim için 100 cümle bulacak fonksiyonları çağırarak işlemi bitiriyorum.
![main](https://github.com/mecitusda/DogalDilisleme/assets/92247286/ceeaae78-f14f-4657-b22c-9ceb0ad75aa6)

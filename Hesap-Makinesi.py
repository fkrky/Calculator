toplama = "+"
cikarma = "-"
carpma = "*"
bolme = "/"

giris1 = int(input("ilk sayiyi  giriniz: "))

giris2 = int(input("İkinci sayiyi giriniz: "))

islem = str(input("islemi seciniz :\n Toplama ise \"+\" simgesini , Çikarma islemini \"-\" simgesi ile , Çarpma islemini \"*\" simgesi ile , bölme islemini \"/\" simgesi ile belirtiniz : "))

if islem == toplama :
    print(giris1+giris2) # Toplama işleminin sonucunu ekrana yansıtır.
elif islem == cikarma :
    print(giris1-giris2) # Çıkarma  işleminin sonucunu ekrana yansıtır.
elif islem == carpma:
    print(giris1*giris2) # Çarpma işleminin sonucunu ekrana yansıtır.
elif islem == bolme :
    print(giris1/giris2) # Bölme işleminin sonucunu ekrana yansıtır.
else: 
    print("Geçersiz simge kullandiniz lütfen sadece *  /  +  -  sembollerini kullaniniz.") 


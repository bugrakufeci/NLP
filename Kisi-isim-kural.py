import time
import logging
import re


paragraf = "Manastırın ana kilisesi olan Daba Kilisesi, Berk Bey inşa edilmiştir. Cmerki Profesör Doçent Berk Dündar. Edirneye köyünün Zeynep Hanım Daba mezrasında Türkiye Büyük Millet Meclisi yer alan kiliseden bugüne pek bir şey kalmamıştır. Grigol Hantsteli’nin Yaşamı adlı elyazmasından Doçent Bartu Can Dündar bilinen Daba Kilisesi’nin olası Ordinaryüs Kemal, yerini Niko Marr 1904’te görmüş, ancak burada bir kilisenin varlığını kesin biçimde tespit edememiştir. Manastırın küçük kilisesi ya da şapeli de aynı yerde bulunuyordu. Niko Marr köyün batısındaki bir tepede bulunan şapelin yıkıntılarını 1904  yılında görmüştü, ancak küçük kilisenin yerinin neresi olduğu bugün bilinmemektedir"
paragraf = paragraf.strip()
Kelimesayisi=paragraf.splitlines()
b=0
for i in Kelimesayisi:
    kelimeler=i.split()
    for a in kelimeler:
        b=b+1
print("--------------------------------------------")
print("paragraf içindeki kelimeler ve adetleri;")
liste = re.split(" |!|\n|\?",paragraf)
kelimesayisi = len(liste)
i=0
k=kelimesayisi
print(k)
#while i <= b:
    #if liste[i] == '':
        #liste.remove(liste[i])
        #b=b-1
    #else:
        #i=i+1
#print(liste)


kelimesayisi=len(liste)
sayac = {}
for kelime in liste:
    if kelime not in sayac:
        sayac[kelime] = 1
    else:
        sayac[kelime] += 1

for key in sayac.keys():
     print("%s %s " % (key, sayac[key]))
print("paragraftaki toplam kelime sayısı:",kelimesayisi)
print("----------------------------------------------------------")
#################################### Ünvandan sonra gelen kişi ismi etiketleme
keywords = open('anahtarOncegelen.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords=i.split(",")
u=-1
for i in keywords: u=u+1 ######### ünvan sayısı
i=0
for i in range(kelimesayisi):
    if liste[i] in keywords and liste[i+1] not in keywords:
        x = liste[i+1]
        x2 = liste[i+2]
        x3 = liste[i+3]
        xS =len(liste[i+1])
        x2S=len(liste[i+2])
        x3S=len(liste[i+3])
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
             print("isim:",liste[i+1])
             yazdır=open('isimListem.txt','a',encoding='utf-8')
             yazdır.write(",")
             yazdır.write(liste[i+1])
             yazdır.close()
             liste[i+1] ="<b_enamex TYPE='PERSON'> " + liste[i+1]
            else:
                if x[xS - 1] == ',':
                 x = x.replace(',','')
                 print("isim:",x)
                 yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                 yazdır.write(",")
                 yazdır.write(x)
                 yazdır.close()
                 liste[i + 1] ="<b_enamex TYPE='PERSON'> " + liste[i + 1] + " <e_enamex>"
                 continue
                elif x[xS - 1] == '.':
                    x = x.replace('.','')
                    print("isim:",x)
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    liste[i + 1] = "<b_enamex TYPE='PERSON'> " + liste[i + 1] + " <e_enamex>"
                    continue
        else:
           continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2 [x2S - 1] != '.':
                print("isim devamı:",liste[i+2])
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i + 2])
                yazdır.close()
                liste[i + 2] = liste[i + 2]
            else:
                if x2[x2S - 1] == ',':
                 x2 = x2.replace(',','')
                 print("isim devamı:",x2)
                 yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                 yazdır.write(",")
                 yazdır.write(x2)
                 yazdır.close()
                 liste[i + 2] =liste[i + 2] + " <e_enamex>"
                 continue
                elif x2[x2S - 1] == '.':
                    x2 = x2.replace('.','')
                    print("isim devamı:",x2)
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    liste[i + 2] =liste[i + 2] + " <e_enamex>"
                    continue


        else:
                continue
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
                print("isim devamı:",liste[i+3])
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i + 3])
                yazdır.close()
                liste[i + 3] =liste[i + 3] + " <e_enamex>"
            else:
                if x3[x3S - 1] == ',':
                 x3 = x3.replace(',','')
                 print("isim devamı:",x3)
                 yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                 yazdır.write(",")
                 yazdır.write(x3)
                 yazdır.close()
                 liste[i + 3] =liste[i + 3] + " <e_enamex>"
                 continue
                elif x3[x3S - 1] == '.':
                    x3 = x3.replace('.','')
                    print("isim devamı:",x3)
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    liste[i + 3] =liste[i + 3] + " <e_enamex>"
                    continue

        else:
            continue
    else:
     continue

#################################### Ünvandan önce gelen kişi ismi etiketleme
keywords = open('anahtarSonragelen.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords=i.split(",")
u=-1
for i in keywords: u=u+1 ######### ünvan sayısı
i=0
for i in range(kelimesayisi):
    if liste[i] in keywords:
        x = liste[i - 3]
        x2 = liste[i - 2]
        x3 = liste[i - 1]
        xS = len(liste[i - 3])
        x2S = len(liste[i - 2])
        x3S = len(liste[i - 1])
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
             print("isim:",liste[i-1])
             yazdır = open('isimListem.txt', 'a', encoding='utf-8')
             yazdır.write(",")
             yazdır.write(liste[i - 1])
             yazdır.close()
             liste[i - 1] = "< " + liste[i - 1] + " B-Person>"
            else:
                    continue

        else:
            continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2 [x2S - 1] != '.':
             print("isim devamı:", liste[i - 2])
             yazdır = open('isimListem.txt', 'a', encoding='utf-8')
             yazdır.write(",")
             yazdır.write(liste[i - 2])
             yazdır.close()
             liste[i - 2] = "< " + liste[i - 2] + " B-Person>"
            else:
                    continue

        else:
            continue
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
             print("isim devamı:", liste[i - 3])
             yazdır = open('isimListem.txt', 'a', encoding='utf-8')
             yazdır.write(",")
             yazdır.write(liste[i - 3])
             yazdır.close()
             liste[i - 3] = "< " + liste[i - 3] + " B-Person>"
            else:
                    continue

        else:
            continue
    else:
        continue


print("----------------------------------------------------------------------")
keywords = open('kurumAnahtar.txt', 'r', encoding='utf-8')
kurumAnahtarsayisi = keywords.readlines()
for i in kurumAnahtarsayisi:
        keywords = i.split(",")
        u = -1
        for i in keywords: u = u + 1
        i = 0
        for i in range(kelimesayisi):
            if liste[i] in keywords:
                x = liste[i - 3]
                x2 = liste[i - 2]
                x3 = liste[i - 1]
                x4 = liste[i]
                if x[0].isupper() == 1:
                    print("Kurum ismi:", liste[i - 3])
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(liste[i - 3])
                    yazdır.close()
                else:
                    continue
                if x2[0].isupper() == 1:
                    print("Kurum ismi devamı:", liste[i - 2])
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(liste[i - 2])
                    yazdır.close()
                else:
                    continue
                if x3[0].isupper() == 1:
                    print("Kurum ismi devamı:", liste[i - 1])
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(liste[i - 1])
                    yazdır.close()
                else:
                    continue
                if x4[0].isupper() == 1:
                    print("Kurum niteliği:", liste[i])
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(liste[i])
                    yazdır.close()
                else:
                    continue
            else:
                continue

        #son = open('etiketli.txt', 'a', encoding='utf-8')
        #i=0
        #sonkelimesayisi = len(liste)
        #while i <= sonkelimesayisi:
            #son.write(liste[i])
            #son.write(" ")
            #i = i + 1
        #son.close()
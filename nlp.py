import json

paragraf = 'Afyonkarahisar’ın Dinar ilçesinde, tır ile otomobilin çarpıştığı kazada, Vehbi Özen ve eşi Ayşe Özen, ' \
           'kayınvalidesi Cemile Kılıçaslan ile 9 yaşındaki çocukları hayatını kaybetti. Kazada hafif yaralanan tır ' \
           'Akdeniz. sürücüsü Murat K. ise ayakta tedavi edildi. Erciyes dağı. '

# TODO Anahtar kelime listeleri txt dosyasına aktarılmalı

anahtarKelimeListesi1 = [
    "kuzey",
    "Kuzey"
    "güney",
    "Güney",
    "Doğu"
    "doğu",
    "batı",
    "Batı"
    "dağ",
    "deniz",
    "göl",
    "sıradağ",
    "ova",
    "okyanus",
    "körfez",
    "tepe",
    "köprü",
    "boğaz",
    "kanal",
    "başkent",
    "ilçe"
]

anahtarKelimeListesi2 = [
    "durak",
    "durağı",
    "dağ",
    "cadde",
    "sokak",
    "köy",
    "mahalle",
    "polikliniği",
    "karakolu",
    "müzesi",
    "tiyatrosu",
    "nehri",
    "cezaevi",
    "hastanesi",
    "bulvarı",
    "viyadükü",
    "otogarı",
    "garı",
    "havaalanı",
    "limanı",
    "kafe",
    "merkezi",
    "tesisi",
    "stadyumu",
    "parkı",
    "sahili",
    "sahil"
    "plaj",
    "daire",
    "büro",
    "lise",
    "ilkokul",
    "ortaokul",
    "üniversite",
    "atölye",
    "otel",
    "pansiyon",
    "hamam",
    "galeri",
    "market",
    "mezarlık",
    "banka",
    "cami",
    "cemevi",
    "kilise",
    "katedral",
    "şapel",
    "istasyon",
    "saray",
    "iskele",
    "yalı",
    "köşk",
    "kasrı",
    "kampüs",
    "yerleşke",
    "orman",
    "baraj"
]

anahtarKelimeListesi3 = ["köy", "deniz", "doğu"]

ulkeListesi = [
    'Türkiye', 'ABD Virgin Adaları', 'Afganistan', 'Aland Adaları',
    'Almanya', 'Amerika Birleşik Devletleri', 'Amerika Birleşik Devletleri Küçük Dış Adaları',
    'Amerikan Samoası',
    'Andora',
    'Angola',
    'Anguilla',
    'Antarktika',
    'Antigua ve Barbuda',
    'Arjantin',
    'Arnavutluk',
    'Aruba',
    'Avrupa Birliği',
    'Avustralya',
    'Avusturya',
    'Azerbaycan',
    'Bahamalar',
    'Bahreyn',
    'Bangladeş',
    'Barbados',
    'Batı Sahara',
    'Belize',
    'Belçika',
    'Benin',
    'Bermuda',
    'Beyaz Rusya',
    'Bhutan',
    'Bilinmeyen veya Geçersiz Bölge',
    'Birleşik Arap Emirlikleri',
    'Birleşik Krallık',
    'Bolivya',
    'Bosna Hersek',
    'Botsvana',
    'Bouvet Adası',
    'Brezilya',
    'Brunei',
    'Bulgaristan',
    'Burkina Faso',
    'Burundi',
    'Cape Verde',
    'Cebelitarık',
    'Cezayir',
    'Christmas Adası',
    'Cibuti',
    'Cocos Adaları',
    'Cook Adaları',
    'Çad',
    'Çek Cumhuriyeti',
    'Çin',
    'Danimarka',
    'Dominik',
    'Dominik Cumhuriyeti',
    'Doğu Timor',
    'Ekvator',
    'Ekvator Ginesi',
    'El Salvador',
    'Endonezya',
    'Eritre',
    'Ermenistan',
    'Estonya',
    'Etiyopya',
    'Falkland Adaları (Malvinalar)',
    'Faroe Adaları',
    'Fas',
    'Fiji',
    'Fildişi Sahilleri',
    'Filipinler',
    'Filistin Bölgesi',
    'Finlandiya',
    'Fransa',
    'Fransız Guyanası',
    'Fransız Güney Bölgeleri',
    'Fransız Polinezyası',
    'Gabon',
    'Gambia',
    'Gana',
    'Gine',
    'Gine-Bissau',
    'Granada',
    'Grönland',
    'Guadeloupe',
    'Guam',
    'Guatemala',
    'Guernsey',
    'Guyana',
    'Güney Afrika',
    'Güney Georgia ve Güney Sandwich Adaları',
    'Güney Kore',
    'Güney Kıbrıs Rum Kesimi',
    'Gürcistan',
    'Haiti',
    'Heard Adası ve McDonald Adaları',
    'Hindistan',
    'Hint Okyanusu İngiliz Bölgesi',
    'Hollanda',
    'Hollanda Antilleri',
    'Honduras',
    'Hong Kong SAR - Çin',
    'Hırvatistan',
    'Irak',
    'İngiliz Virgin Adaları',
    'İran',
    'İrlanda',
    'İspanya',
    'İsrail',
    'İsveç',
    'İsviçre',
    'İtalya',
    'İzlanda',
    'Jamaika',
    'Japonya',
    'Jersey',
    'Kamboçya',
    'Kamerun',
    'Kanada',
    'Karadağ',
    'Katar',
    'Kayman Adaları',
    'Kazakistan',
    'Kenya',
    'Kiribati',
    'Kolombiya',
    'Komorlar',
    'Kongo',
    'Kongo Demokratik Cumhuriyeti',
    'Kosta Rika',
    'Kuveyt',
    'Kuzey Kore',
    'Kuzey Mariana Adaları',
    'Küba',
    'Kırgızistan',
    'Laos',
    'Lesotho',
    'Letonya',
    'Liberya',
    'Libya',
    'Liechtenstein',
    'Litvanya',
    'Lübnan',
    'Lüksemburg',
    'Macaristan',
    'Madagaskar',
    'Makao S.A.R. Çin',
    'Makedonya',
    'Malavi',
    'Maldivler',
    'Malezya',
    'Mali',
    'Malta',
    'Man Adası',
    'Marshall Adaları',
    'Martinik',
    'Mauritius',
    'Mayotte',
    'Meksika',
    'Mikronezya Federal Eyaletleri',
    'Moldovya Cumhuriyeti',
    'Monako',
    'Montserrat',
    'Moritanya',
    'Mozambik',
    'Moğolistan',
    'Myanmar',
    'Mısır',
    'Namibya',
    'Nauru',
    'Nepal',
    'Nijer',
    'Nijerya',
    'Nikaragua',
    'Niue',
    'Norfolk Adası',
    'Norveç',
    'Orta Afrika Cumhuriyeti',
    'Özbekistan',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua Yeni Gine',
    'Paraguay',
    'Peru',
    'Pitcairn',
    'Polonya',
    'Portekiz',
    'Porto Riko',
    'Reunion',
    'Romanya',
    'Ruanda',
    'Rusya Federasyonu',
    'Saint Helena',
    'Saint Kitts ve Nevis',
    'Saint Lucia',
    'Saint Pierre ve Miquelon',
    'Saint Vincent ve Grenadinler',
    'Samoa',
    'San Marino',
    'Sao Tome ve Principe',
    'Senegal',
    'Seyşeller',
    'Sierra Leone',
    'Singapur',
    'Slovakya',
    'Slovenya',
    'Solomon Adaları',
    'Somali',
    'Sri Lanka',
    'Sudan',
    'Surinam',
    'Suriye',
    'Suudi Arabistan',
    'Svalbard ve Jan Mayen',
    'Svaziland',
    'Sırbistan',
    'Sırbistan-Karadağ',
    'Şili',
    'Tacikistan',
    'Tanzanya',
    'Tayland',
    'Tayvan',
    'Togo',
    'Tokelau',
    'Tonga',
    'Trinidad ve Tobago',
    'Tunus',
    'Turks ve Caicos Adaları',
    'Tuvalu',
    'Türkmenistan',
    'Uganda',
    'Ukrayna',
    'Umman',
    'Uruguay',
    'Uzak Okyanusya',
    'Ürdün',
    'Vanuatu',
    'Vatikan',
    'Venezuela',
    'Vietnam',
    'Wallis ve Futuna',
    'Yemen',
    'Yeni Kaledonya',
    'Yeni Zelanda',
    'Yunanistan',
    'Zambiya',
    'Zimbabve'
]
# TODO Şehir listesi JSON dosyasından çekilmeli ve kullanılmalı
sehirListesi = []

#with open('cities.json', 'rb') as data_file:
#    data = json.load(data_file)
#    print(data)

# print ('Retrieved', len(data), 'characters')
# parsed_json = (json.loads(data.decode("utf-8")))
# sehirDosyasi.close()

# for i in range(len(sehirData["cities"])):
#    sehirListesi.append(sehirData['cities'][i]['name'])

#print(len(sehirListesi))

isaretlenmisKelimeListesi = []
print(paragraf)
paragraf = paragraf.strip()
kelimeListesi = paragraf.split(" ")

# Kelimelerin aynı zamanda büyük harfleri versiyonları listeye ekleniyor. Örn: (dağ > Dağ)
for i in range(len(anahtarKelimeListesi2)):
    anahtarKelimeListesi2.append(anahtarKelimeListesi2[i].capitalize())


for i in range(len(kelimeListesi)):
    kelime = kelimeListesi[i]
    kelime = kelime.replace(",", "")
    kelime = kelime.replace(".", "")

    # Kural 1 : Aşağıda belirtilen (anahtarKelimeListesi1) ifadelerden herhangi biri büyük harfle başlayan bir
    # kelimeden önce veya sonra yer alıyorsa işaretlenir:
    for j in range(len(anahtarKelimeListesi1)):
        if (kelimeListesi[i] == anahtarKelimeListesi1[j]) | (anahtarKelimeListesi1[j] in kelimeListesi[i]):
            kelimeListesi[i] = kelimeListesi[i].replace(",", "")
            kelimeListesi[i] = kelimeListesi[i].replace(".", "")
            if i >= len(kelimeListesi):
                if kelimeListesi[i + 1][0].isupper():
                    isaretlenmisKelimeListesi.append("%s %s" % (kelimeListesi[i], kelimeListesi[i + 1]))
            elif i != 0:
                if kelimeListesi[i - 1][0].isupper():
                    isaretlenmisKelimeListesi.append("%s %s" % (kelimeListesi[i - 1], kelimeListesi[i]))
    # Kural 2 : Aşağıdaki ifadelerden (anahtarKelimeListesi2) herhangi biri metinde bulunuyorsa, ifadeden önce yer
    # alan ardışık büyük harfle başlayan kelimeler işaretlenir:
    for j in range(len(anahtarKelimeListesi2)):
        if (kelimeListesi[i] == anahtarKelimeListesi2[j]) | (anahtarKelimeListesi2[j] in kelimeListesi[i]):
            kelimeListesi[i] = kelimeListesi[i].replace(",", "")
            kelimeListesi[i] = kelimeListesi[i].replace(".", "")
            if (i >= 1) & (kelimeListesi[i - 1][0].isupper()):
                if (i >= 2) & (kelimeListesi[i - 2][0].isupper()):
                    if (i >= 3) & (kelimeListesi[i - 3][0].isupper()):
                        if (i >= 4) & (kelimeListesi[i - 4][0].isupper()):
                            isaretlenmisKelimeListesi.append("%s %s %s %s %s" % (kelimeListesi[i - 4],
                                                                                 kelimeListesi[i - 3],
                                                                                 kelimeListesi[i - 2],
                                                                                 kelimeListesi[i - 1],
                                                                                 kelimeListesi[i]))
                        else:
                            isaretlenmisKelimeListesi.append("%s %s %s %s" % (kelimeListesi[i - 3],
                                                                              kelimeListesi[i - 2],
                                                                              kelimeListesi[i - 1],
                                                                              kelimeListesi[i]))
                    else:
                        isaretlenmisKelimeListesi.append("%s %s %s" % (kelimeListesi[i - 2], kelimeListesi[i - 1],
                                                                       kelimeListesi[i]))

                else:
                    isaretlenmisKelimeListesi.append("%s %s" % (kelimeListesi[i - 1], kelimeListesi[i]))

    # Kural 3 : Aşağıdaki ifadelerden (anahtarKelimeListesi3) biri kelimenin içinde yer alıyorsa (kelime bileşikse)
    # kelimenin tamamı işaretlenir:
    for j in range(len(anahtarKelimeListesi3)):
        if anahtarKelimeListesi3[j] in kelimeListesi[i]:
            isaretlenmisKelimeListesi.append(kelime)

    # Kural 4 : ‘de, ’da, ’den, ’dan, ’te, ’ta eklerinden önce büyük harfle başlayan bir kelime
    # varsa yer olarak işaretlenir.
    if ("’" in kelime) & (kelime[0].isupper()):
        isaretlenmisKelimeListesi.append(kelime.split("’")[0])
    elif ("'" in kelime) & (kelime[0].isupper()):
        isaretlenmisKelimeListesi.append(kelime.split("'")[0])

    kelimeListesi[i] = kelime

# TODO isaretlenmisKelimeListesi duplicate bulundurmamalı.

# Yer ismi işaretleme burada bitiyor.

kelimesayisi = len(kelimeListesi)

print("paragraftaki toplam kelime sayısı:", len(kelimeListesi))
print("----------------------------------------------------------")

#################################### Ünvandan sonra gelen kişi ismi etiketleme
keywords = open('anahtarOncegelen.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords = i.split(",")
u = -1
for i in keywords: u = u + 1  ######### ünvan sayısı
i = 0
for i in range(kelimesayisi):
    if kelimeListesi[i] in keywords and kelimeListesi[i + 1] not in keywords:
        x = kelimeListesi[i + 1]
        x2 = kelimeListesi[i + 2]
        x3 = kelimeListesi[i + 3]
        xS = len(kelimeListesi[i + 1])
        x2S = len(kelimeListesi[i + 2])
        x3S = len(kelimeListesi[i + 3])
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
                print("isim:", kelimeListesi[i + 1])
                yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i + 1])
                yazdir.close()
                kelimeListesi[i + 1] = "<b_enamex TYPE='PERSON'> " + kelimeListesi[i + 1]
            else:
                if x[xS - 1] == ',':
                    x = x.replace(',', '')
                    print("isim:", x)
                    yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdir.write(",")
                    yazdir.write(x)
                    yazdir.close()
                    kelimeListesi[i + 1] = "<b_enamex TYPE='PERSON'> " + kelimeListesi[i + 1] + " <e_enamex>"
                    continue
                elif x[xS - 1] == '.':
                    x = x.replace('.', '')
                    print("isim:", x)
                    yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdir.write(",")
                    yazdir.write(x)
                    yazdir.close()
                    kelimeListesi[i + 1] = "<b_enamex TYPE='PERSON'> " + kelimeListesi[i + 1] + " <e_enamex>"
                    continue
        else:
            continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2[x2S - 1] != '.':
                print("isim devamı:", kelimeListesi[i + 2])
                yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i + 2])
                yazdir.close()
                kelimeListesi[i + 2] = kelimeListesi[i + 2]
            else:
                if x2[x2S - 1] == ',':
                    x2 = x2.replace(',', '')
                    print("isim devamı:", x2)
                    yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdir.write(",")
                    yazdir.write(x2)
                    yazdir.close()
                    kelimeListesi[i + 2] = kelimeListesi[i + 2] + " <e_enamex>"
                    continue
                elif x2[x2S - 1] == '.':
                    x2 = x2.replace('.', '')
                    print("isim devamı:", x2)
                    yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdir.write(",")
                    yazdir.write(x2)
                    yazdir.close()
                    kelimeListesi[i + 2] = kelimeListesi[i + 2] + " <e_enamex>"
                    continue


        else:
            continue
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
                print("isim devamı:", kelimeListesi[i + 3])
                yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i + 3])
                yazdir.close()
                kelimeListesi[i + 3] = kelimeListesi[i + 3] + " <e_enamex>"
            else:
                if x3[x3S - 1] == ',':
                    x3 = x3.replace(',', '')
                    print("isim devamı:", x3)
                    yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdir.write(",")
                    yazdir.write(x3)
                    yazdir.close()
                    kelimeListesi[i + 3] = kelimeListesi[i + 3] + " <e_enamex>"
                    continue
                elif x3[x3S - 1] == '.':
                    x3 = x3.replace('.', '')
                    print("isim devamı:", x3)
                    yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdir.write(",")
                    yazdir.write(x3)
                    yazdir.close()
                    kelimeListesi[i + 3] = kelimeListesi[i + 3] + " <e_enamex>"
                    continue

        else:
            continue
    else:
        continue

#################################### Ünvandan önce gelen kişi ismi etiketleme
keywords = open('anahtarSonragelen.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords = i.split(",")
u = -1
for i in keywords: u = u + 1  ######### ünvan sayısı
i = 0
for i in range(kelimesayisi):
    if kelimeListesi[i] in keywords:
        x = kelimeListesi[i - 3]
        x2 = kelimeListesi[i - 2]
        x3 = kelimeListesi[i - 1]
        xS = len(kelimeListesi[i - 3])
        x2S = len(kelimeListesi[i - 2])
        x3S = len(kelimeListesi[i - 1])
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
                print("isim:", kelimeListesi[i - 1])
                yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i - 1])
                yazdir.close()
                kelimeListesi[i - 1] = "< " + kelimeListesi[i - 1] + " B-Person>"
            else:
                continue

        else:
            continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2[x2S - 1] != '.':
                print("isim devamı:", kelimeListesi[i - 2])
                yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i - 2])
                yazdir.close()
                kelimeListesi[i - 2] = "< " + kelimeListesi[i - 2] + " B-Person>"
            else:
                continue

        else:
            continue
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
                print("isim devamı:", kelimeListesi[i - 3])
                yazdir = open('isimListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i - 3])
                yazdir.close()
                kelimeListesi[i - 3] = "< " + kelimeListesi[i - 3] + " B-Person>"
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
        if kelimeListesi[i] in keywords:
            x = kelimeListesi[i - 3]
            x2 = kelimeListesi[i - 2]
            x3 = kelimeListesi[i - 1]
            x4 = kelimeListesi[i]
            if x[0].isupper() == 1:
                print("Kurum ismi:", kelimeListesi[i - 3])
                yazdir = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i - 3])
                yazdir.close()
            else:
                continue
            if x2[0].isupper() == 1:
                print("Kurum ismi devamı:", kelimeListesi[i - 2])
                yazdir = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i - 2])
                yazdir.close()
            else:
                continue
            if x3[0].isupper() == 1:
                print("Kurum ismi devamı:", kelimeListesi[i - 1])
                yazdir = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i - 1])
                yazdir.close()
            else:
                continue
            if x4[0].isupper() == 1:
                print("Kurum niteliği:", kelimeListesi[i])
                yazdir = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdir.write(",")
                yazdir.write(kelimeListesi[i])
                yazdir.close()
            else:
                continue
        else:
            continue

    # son = open('etiketli.txt', 'a', encoding='utf-8')
    # i=0
    # sonkelimesayisi = len(liste)
    # while i <= sonkelimesayisi:
    # son.write(liste[i])
    # son.write(" ")
    # i = i + 1
    # son.close()

print("Yer için işaretlenmiş kelime listesi: ")
print(isaretlenmisKelimeListesi)

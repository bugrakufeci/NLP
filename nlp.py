import json
import re
from nltk import tokenize


f = open('nerdatanotag.txt', 'r', encoding='utf8')
paragraf = f.read()
f.close()

# TODO Anahtar kelime listeleri txt dosyasına aktarılmalı

# Bu kelime listesi işaretlenmesi gereken kelimeden önce gelebilecek kelimeleri kapsar. Örn : Kuzey Amerika
anahtarKelimeListesi1 = [
    "Kuzey",
    "Güney",
    "Doğu",
    "Batı",
    "Deniz",
    "Göl",
    "Sıradağ",
    "Ova",
    "Okyanus",
    "Körfez",
    "Tepe",
    "Köprü",
    "Boğaz",
    "Kanal",
    "başkent",
    "ilçe"
]

# Bu kelime listesi işaretlenmesi gereken kelimeden sonra gelen kelimeleri kapsar. Örn: Topkapı Sarayı
anahtarKelimeListesi2 = [
    "pist",
    "site",
    "durağı",
    "Dağ",
    "Cadde",
    "Sokak",
    "Üniversite",
    "Köy",
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
    "tesisi",
    "Stadyumu",
    "Stad",
    "parkı",
    "Meyhane",
    "Sahili",
    "Plajı",
    "Cafe",
    "Otel",
    "Pansiyon",
    "Hamam",
    "Market",
    "mezarlığı",
    "cami",
    "manastır",
    "Salon",
    "cemevi",
    "kilise",
    "katedral",
    "şapel",
    "istasyon",
    "Sarayı",
    "Burnu",
    "iskele",
    "Yalı",
    "Köşk",
    "Kasrı",
    "Kampüs",
    "yerleşke",
    "Orman",
    "Baraj"
]

# Bu kelime listesi bitişik halde bulunduğunda işaretlenmesi gereken kelimeleri kapsar. Örn : Ortadoğu
anahtarKelimeListesi3 = ["köy", "deniz", "doğu", "istan"]

# Bu kelime listesi ek alan kelimenin içermemesi gereken kelimeleri kapsar. Örn: Trabzonspor'a
anahtarKelimeListesi4 = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim",
                         "kasım", "aralık" "spor", "festival", "kupa", "lig", "şölen", "balo"]

ulkeListesi = [
    'Türkiye', 'ABD Virgin Adaları', 'Afganistan', 'Aland Adaları',
    'Almanya', 'Amerika Birleşik Devletleri', 'Amerika Birleşik Devletleri Küçük Dış Adaları',
    'Amerikan Samoası',
    'ABD',
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
    'Osmanlı',
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
    'Belarus',
    'Bhutan',
    'Birleşik Arap Emirlikleri',
    'BAE',
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
    'Çekya',
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
    'Falkland Adaları',
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
    'Kuzey Kıbrıs Türk Cumhuriyeti',
    'Hollanda',
    'Hollanda Antilleri',
    'Honduras',
    'Hong Kong',
    'Hırvatistan',
    'Kuzey Irak',
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
    'Kongo',
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
    'Afrika',
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
    'Rusya',
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
sehirListesi = []

f = open('turkiyesehirler.json', encoding='utf-8')
data = json.load(f)
for i in data['cities']:
    sehirListesi.append(i['name'])
f.close()

isaretlenenYerIsimleri = []
paragraf = paragraf.strip()
islenmemisKelimeler = paragraf.split(" ")
kelimeListesi = []

print("Kelimeler temizleniyor ve ayıklanıyor.")
for i in range(len(islenmemisKelimeler)):
    islenmemisKelimeler[i] = islenmemisKelimeler[i].strip()
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace(",", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace(".", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace("(", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace(")", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace('"', "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace("#", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace(" ", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace(";", "")
    islenmemisKelimeler[i] = islenmemisKelimeler[i].replace(":", "")
    if len(islenmemisKelimeler[i]) > 1:
        kelimeListesi.append(islenmemisKelimeler[i])

# Kelimelerin aynı zamanda büyük harfleri versiyonları listeye ekleniyor. Örn: (dağ > Dağ)
for i in range(len(anahtarKelimeListesi2)):
    anahtarKelimeListesi2.append(anahtarKelimeListesi2[i].capitalize())

print("Yer işaretleme gerçekleştiriliyor.")
for i in range(len(kelimeListesi)):

    if i == 10000:
        print("10.000 kelime işlendi.")
    if i == 50000:
        print("50.000 kelime işlendi.")
    if i == 100000:
        print("100.000 kelime işlendi.")
    if i == 200000:
        print("200.000 kelime işlendi.")
    if i == 300000:
        print("300.000 kelime işlendi.")
    if i == 400000:
        print("400.000 kelime işlendi.")

    shouldContinue = False
    if (kelimeListesi[i] != " ") | (kelimeListesi[i] != "  ") | (kelimeListesi[i] != ' "') | (kelimeListesi[i] != '" '):
        kelime = kelimeListesi[i]

    # Kural 3 : Aşağıdaki ifadelerden (anahtarKelimeListesi3) biri kelimenin içinde yer alıyorsa (kelime bileşikse)
    # kelimenin tamamı işaretlenir:
    for j in range(len(anahtarKelimeListesi3)):
        if (anahtarKelimeListesi3[j] in kelimeListesi[i]) & (kelimeListesi[i] != anahtarKelimeListesi3[j]) & (
                kelimeListesi[i][0].isupper()):
            isaretlenenYerIsimleri.append(kelimeListesi[i])
            shouldContinue = True

    if shouldContinue:
        continue
    # Kural 1 : Aşağıda belirtilen (anahtarKelimeListesi1) ifadelerden herhangi biri büyük harfle başlayan bir
    # kelimeden önce veya sonra yer alıyorsa işaretlenir:
    for j in range(len(anahtarKelimeListesi1)):
        if (kelimeListesi[i] == anahtarKelimeListesi1[j]) | (anahtarKelimeListesi1[j] in kelimeListesi[i]):

            if kelimeListesi[i + 1][0].isupper():
                isaretlenenYerIsimleri.append("%s %s" % (kelimeListesi[i], kelimeListesi[i + 1]))
                shouldContinue = True
            if i != 0:
                if kelimeListesi[i - 1][0].isupper():
                    isaretlenenYerIsimleri.append("%s %s" % (kelimeListesi[i - 1], kelimeListesi[i]))
                    shouldContinue = True
    if shouldContinue:
        continue
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
                            isaretlenenYerIsimleri.append("%s %s %s %s %s" % (kelimeListesi[i - 4],
                                                                              kelimeListesi[i - 3],
                                                                              kelimeListesi[i - 2],
                                                                              kelimeListesi[i - 1],
                                                                              kelimeListesi[i]))
                            break

                        else:
                            isaretlenenYerIsimleri.append("%s %s %s %s" % (kelimeListesi[i - 3],
                                                                           kelimeListesi[i - 2],
                                                                           kelimeListesi[i - 1],
                                                                           kelimeListesi[i]))
                            break
                    else:
                        isaretlenenYerIsimleri.append("%s %s %s" % (kelimeListesi[i - 2], kelimeListesi[i - 1],
                                                                    kelimeListesi[i]))
                        break
                else:
                    isaretlenenYerIsimleri.append("%s %s" % (kelimeListesi[i - 1], kelimeListesi[i]))
                    shouldContinue = True
                    break

    if shouldContinue:
        continue

    if kelimeListesi[i][0].isupper():
        for j in range(len(ulkeListesi)):
            if "'" in kelimeListesi[i]:
                if ulkeListesi[j] in kelimeListesi[i].split("'")[0]:
                    isaretlenenYerIsimleri.append(kelimeListesi[i])
                    shouldContinue = True
            if ulkeListesi[j] == kelimeListesi[i]:
                isaretlenenYerIsimleri.append(kelimeListesi[i])
                shouldContinue = True
            if ulkeListesi[j].upper() == kelimeListesi[i]:
                isaretlenenYerIsimleri.append(kelimeListesi[i])
                shouldContinue = True

    if shouldContinue:
        continue

    if kelimeListesi[i][0].isupper():
        for j in range(len(sehirListesi)):
            if "'" in kelimeListesi[i]:
                if sehirListesi[j] == kelimeListesi[i].split("'")[0]:
                    isaretlenenYerIsimleri.append(kelimeListesi[i])
            if sehirListesi[j] == kelimeListesi[i]:
                isaretlenenYerIsimleri.append(kelimeListesi[i])
            if sehirListesi[j].upper() == kelimeListesi[i]:
                isaretlenenYerIsimleri.append(kelimeListesi[i])

print("Yer işaretleme tamamlandı.İşaretlenen yer ismi sayısı: ")
print(len(isaretlenenYerIsimleri))

isaretlenmisParaListesi = []


def get_amount(word_list):
    processed_list = []
    # remove comma
    for word in word_list:
        processed_list.append(word.replace(',', ''))

    if not processed_list[0].replace('.', '').replace(',', '').replace('-', '').isnumeric() and processed_list[
        0] not in transformations:
        return False, 0

    return True, ' '.join(processed_list)


transformations = [
    "bin",
    "milyon",
    "milyar",
    "trilyon"
]
currencies = open('currencies.txt', encoding='utf-8').read().lower().split('\n')
input_lines = paragraf.lower().split('\n')
input_words = []
for line in input_lines:
    input_words += line.split(' ')

    # O(n^2)
for i in range(len(input_words)):
    for currency in currencies:
        if str(input_words[i]).startswith(currency) and (i > 0 and (
                input_words[i - 1].replace('-', '').replace('.', '').isnumeric() or input_words[i - 1] in
                transformations)):
            first_index = i
            while True:
                is_available, amount_new = get_amount(input_words[first_index - 1:i])
                if not is_available:
                    break
                amount = amount_new
                first_index -= 1
            isaretlenmisParaListesi.append(f"{amount} {currency}")
print("Para işaretleme tamamlandı. İşaretlenen para sayısı:")
print(len(isaretlenmisParaListesi))

Kelimesayisi = paragraf.splitlines()
isaretliKisiListesi = []

print("Kişi işaretleme üzerinde çalışılıyor...")
b = 0
for i in Kelimesayisi:
    kelimeler = i.split()
    for a in kelimeler:
        b = b + 1

liste = paragraf.split()
kelimesayisi = len(liste)
i = 0
k = kelimesayisi
kelimesayisi = len(liste)
sayac = {}
for kelime in liste:
    if kelime not in sayac:
        sayac[kelime] = 1
    else:
        sayac[kelime] += 1

p = open('isimler.txt', 'r', encoding='utf-8')
isimler = p.read().splitlines()
i = 0
isimsayac = 0
for i in range(kelimesayisi):
    if liste[i].upper() in isimler and liste[i + 1].upper() not in isimler and liste[i + 1][0].isupper() == 1:
        liste[i] = "<b_enamex TYPE='PERSON'> " + liste[i] + " <e_enamex>"
        isimsayac += 1
        isaretliKisiListesi.append(f"{liste[i]}")
    elif liste[i].upper() in isimler and liste[i + 1].upper() in isimler and liste[i + 2].upper() not in isimler and \
            liste[i + 1][0].isupper() == 1 and liste[i + 2][0].isupper() == 1:
        isimsayac += 1
        isaretliKisiListesi.append(f"{liste[i]} {liste[i + 1]}")
    elif liste[i].upper() in isimler and liste[i + 1].upper() in isimler and liste[i + 2].upper() in isimler and \
            liste[i + 1][0].isupper() == 1 and liste[i + 2][0].isupper() == 1 and liste[i + 3][0].isupper() == 1:
        isimsayac += 1
        isaretliKisiListesi.append(f"{liste[i]} {liste[i + 1]} {liste[i + 2]}")
keywords = open('anahtarOncegelen.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords = i.split(",")
u = -1
for i in keywords: u = u + 1  # ünvan sayısı
i = 0
for i in range(kelimesayisi):
    if liste[i] in keywords and liste[i + 1] not in keywords:
        x = liste[i + 1]
        x2 = liste[i + 2]
        x3 = liste[i + 3]
        xS = len(liste[i + 1])
        x2S = len(liste[i + 2])
        x3S = len(liste[i + 3])
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i + 1])
                yazdır.close()
                liste[i + 1] = "<b_enamex TYPE='PERSON'> " + liste[i + 1]
            else:
                if x[xS - 1] == ',':
                    x = x.replace(',', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i]} {liste[i + 1]}")
                    liste[i + 1] = "<b_enamex TYPE='PERSON'> " + liste[i + 1] + " <e_enamex>"
                    isimsayac += 1

                    continue
                elif x[xS - 1] == '.':
                    x = x.replace('.', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i + 1]}")
                    liste[i + 1] = "<b_enamex TYPE='PERSON'> " + liste[i + 1] + " <e_enamex>"
                    isimsayac += 1

                    continue
        else:
            continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2[x2S - 1] != '.':
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i + 2])
                yazdır.close()
            else:
                if x2[x2S - 1] == ',':
                    x2 = x2.replace(',', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i + 1]} {liste[i + 2]}")
                    liste[i + 2] = liste[i + 2] + " <e_enamex>"
                    isimsayac += 1

                    continue
                elif x2[x2S - 1] == '.':
                    x2 = x2.replace('.', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i + 1]} {liste[i + 2]}")
                    liste[i + 2] = liste[i + 2] + " <e_enamex>"
                    isimsayac += 1

                    continue


        else:
            isaretliKisiListesi.append(f"{liste[i + 1]}")
            liste[i + 1] = liste[i + 1] + " <e_enamex>"
            isimsayac += 1

            continue
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i + 3])
                yazdır.close()
                isaretliKisiListesi.append(f"{liste[i + 1]} {liste[i + 2]} {liste[i + 3]}")
                liste[i + 3] = liste[i + 3] + " <e_enamex>"

                isimsayac += 1
            else:
                if x3[x3S - 1] == ',':
                    x3 = x3.replace(',', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i + 1]} {liste[i + 2]} {liste[i + 3]}")
                    liste[i + 3] = liste[i + 3] + " <e_enamex>"
                    isimsayac += 1

                    continue
                elif x3[x3S - 1] == '.':
                    x3 = x3.replace('.', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i + 1]} {liste[i + 2]} {liste[i + 3]}")
                    liste[i + 3] = liste[i + 3] + " <e_enamex>"
                    isimsayac += 1

                    continue

        else:
            isaretliKisiListesi.append(f"{liste[i + 1]} {liste[i + 2]}")
            liste[i + 2] = liste[i + 2] + " <e_enamex>"
            isimsayac += 1

            continue
    else:
        continue
keywords = open('anahtarsonragelen.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords = i.split(",")
u = -1
for i in keywords: u = u + 1  # ünvan sayısı
i = 0
for i in range(kelimesayisi):
    if liste[i] in keywords and liste[i + 1] not in keywords:
        x = liste[i - 1]
        x2 = liste[i - 2]
        x3 = liste[i - 3]
        xS = len(liste[i - 1])
        x2S = len(liste[i - 2])
        x3S = len(liste[i - 3])
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i - 1])
                yazdır.close()
                liste[i - 1] = liste[i - 1] + " <e_enamex>"
            else:
                if x[xS - 1] == ',':
                    x = x.replace(',', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i - 1]}")
                    liste[i - 1] = "<b_enamex TYPE='PERSON'> " + liste[i - 1] + " <e_enamex>"
                    isimsayac += 1

                    continue
                elif x[xS - 1] == '.':
                    x = x.replace('.', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i - 1]}")
                    liste[i - 1] = "<b_enamex TYPE='PERSON'> " + liste[i - 1] + " <e_enamex>"
                    isimsayac += 1

                    continue
        else:
            continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2[x2S - 1] != '.':
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i - 2])
                yazdır.close()
            else:
                if x2[x2S - 1] == ',':
                    x2 = x2.replace(',', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i - 2]} {liste[i - 1]}")
                    liste[i - 2] = "<b_enamex TYPE='PERSON'> " + liste[i - 2]
                    isimsayac += 1

                    continue
                elif x2[x2S - 1] == '.':
                    x2 = x2.replace('.', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i - 2]} {liste[i - 1]}")
                    liste[i - 2] = "<b_enamex TYPE='PERSON'> " + liste[i - 2]
                    isimsayac += 1

                    continue


        else:
            isaretliKisiListesi.append(f"{liste[i - 1]}")
            liste[i - 1] = "<b_enamex TYPE='PERSON'> " + liste[i - 1]
            isimsayac += 1


            continue
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
                yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i - 3])
                yazdır.close()
                isaretliKisiListesi.append(f"{liste[i - 3]} {liste[i - 2]} {liste[i - 1]}")
                liste[i - 3] = "<b_enamex TYPE='PERSON'> " + liste[i - 3]
                isimsayac += 1

            else:
                if x3[x3S - 1] == ',':
                    x3 = x3.replace(',', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i - 3]} {liste[i - 2]} {liste[i - 1]}")
                    liste[i - 3] = "<b_enamex TYPE='PERSON'> " + liste[i - 3]
                    isimsayac += 1

                    continue
                elif x3[x3S - 1] == '.':
                    x3 = x3.replace('.', '')
                    yazdır = open('isimListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    isaretliKisiListesi.append(f"{liste[i - 3]} {liste[i - 2]} {liste[i - 1]}")
                    liste[i - 3] = "<b_enamex TYPE='PERSON'> " + liste[i - 3]
                    isimsayac += 1

                    continue

        else:
            isaretliKisiListesi.append(f"{liste[i - 2]} {liste[i - 1]}")
            liste[i - 2] = "<b_enamex TYPE='PERSON'> " + liste[i - 2]

            isimsayac += 1
            continue
    else:
        continue

print("Kişi işaretleme tamamlandı. İşaretlenen kişi sayısı: ")
print(len(isaretliKisiListesi))

isaretlenenKurumListesi = []

print("Kurum isimleri üzerinde çalışılıyor...")
keywords = open('kurumAnahtar.txt', 'r', encoding='utf-8')
unvansayisi = keywords.readlines()
for i in unvansayisi:
    keywords = i.split(",")
u = -1
for i in keywords: u = u + 1  ######### ünvan sayısı
i = 0
kurumsayac = 0
for i in range(kelimesayisi):
    if liste[i] in keywords and liste[i + 1] not in keywords:
        x = liste[i - 1]
        x2 = liste[i - 2]
        x3 = liste[i - 3]
        xS = len(liste[i - 1])
        x2S = len(liste[i - 2])
        x3S = len(liste[i - 3])
        if x[0].isupper() == 1:
            if x[xS - 1] != ',' and x[xS - 1] != '.':
                yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i - 1])
                yazdır.close()
                liste[i] = liste[i] + " <e_enamex>"
            else:
                if x[xS - 1] == ',':
                    x = x.replace(',', '')
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    isaretlenenKurumListesi.append(f"{liste[i - 1]} {liste[i]}")
                    liste[i - 1] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 1] + liste[i] + " <e_enamex>"
                    kurumsayac += 1

                    continue
                elif x[xS - 1] == '.':
                    x = x.replace('.', '')
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x)
                    yazdır.close()
                    isaretlenenKurumListesi.append(f"{liste[i - 1]} {liste[i]}")
                    liste[i - 1] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 1] + liste[i] + " <e_enamex>"
                    kurumsayac += 1

                    continue
        else:
            continue
        if x2[0].isupper() == 1:
            if x2[x2S - 1] != ',' and x2[x2S - 1] != '.':
                yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i - 2])
                yazdır.close()
            else:
                if x2[x2S - 1] == ',':
                    x2 = x2.replace(',', '')
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    isaretlenenKurumListesi.append(f"{liste[i - 2]} {liste[i - 1]}")
                    liste[i - 2] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 2]
                    kurumsayac += 1

                    continue
                elif x2[x2S - 1] == '.':
                    x2 = x2.replace('.', '')
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x2)
                    yazdır.close()
                    isaretlenenKurumListesi.append(f"{liste[i - 2]} {liste[i - 1]}")
                    liste[i - 2] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 2]
                    kurumsayac += 1

                    continue


        else:
            liste[i - 1] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 1]
            kurumsayac += 1
            isaretlenenKurumListesi.append(f"{liste[i - 1]}")

            continue
        if x3[0].isupper() == 1:
            if x3[x3S - 1] != ',' and x3[x3S - 1] != '.':
                yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                yazdır.write(",")
                yazdır.write(liste[i - 3])
                yazdır.close()
                isaretlenenKurumListesi.append(f"{liste[i - 3]} {liste[i - 2]} {liste[i - 3]}")
                liste[i - 3] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 3]
                kurumsayac += 1

            else:
                if x3[x3S - 1] == ',':
                    x3 = x3.replace(',', '')
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    isaretlenenKurumListesi.append(f"{liste[i - 3]} {liste[i - 2]} {liste[i - 1]}")
                    liste[i - 3] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 3]
                    kurumsayac += 1

                    continue
                elif x3[x3S - 1] == '.':
                    x3 = x3.replace('.', '')
                    yazdır = open('kurumListem.txt', 'a', encoding='utf-8')
                    yazdır.write(",")
                    yazdır.write(x3)
                    yazdır.close()
                    isaretlenenKurumListesi.append(f"{liste[i - 3]} {liste[i - 2]} {liste[i - 1]}")
                    liste[i - 3] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 3]
                    kurumsayac += 1

                    continue

        else:
            isaretlenenKurumListesi.append(f"{liste[i - 2]} {liste[i - 1]}")
            liste[i - 2] = "<b_enamex TYPE='ORGANIZATION'> " + liste[i - 2]
            kurumsayac += 1

            continue
    else:
        continue

print("Kurum ismi işaretleme tamamlandı.")
print(len(isaretlenenKurumListesi))

print("Tarih ve saat işaretlemeleri yapılıyor.")

isaretlenmisTarihListesi = []


def tarihBul(self):
    aylar = "Ocak|ocak|Şubat|şubat|Mart|mart|nisan|Nisan|mayıs|Mayıs|Haziran|haziran|Temmuz|temmuz|Ağustos|ağustos|Eylül|eylül|Ekim|ekim|Kasım|kasım|aralık|Aralık"
    aylarRakamsal = "\d{2}"

    ayBul = "(" + aylar + "|" + aylarRakamsal + ")"

    ayırıcı1 = "[\s]"
    ayırıcı2 = "[\-]"
    ayırıcı3 = "[\/]"

    ayırıcılar = "(" + ayırıcı1 + "|" + ayırıcı2 + "|" + ayırıcı3 + ")"

    gün1 = "\d{2}"
    gün2 = "\d{1}"

    günler = "(" + gün1 + "|" + gün2 + ")"

    yıl = "\d{4}"

    regex = günler + ayırıcılar + ayBul + ayırıcılar + yıl

    cümleler = tokenize.sent_tokenize(self)
    for cümle in cümleler:
        hepsini_buldum = False
        while  not hepsini_buldum:

            tarih = re.search(regex, cümle)
            if tarih:
                isaretlenmisTarihListesi.append(tarih.group())
                cümle = cümle[tarih.span()[1]:]
            else:
                hepsini_buldum = True

def anahtarBul(self):

   regex="tarih|saat|Saat|dün|evelsi gün|bugün|yarın|yılında|seneye|zaman|pazartesi|salı|çarşamba|perşembe|cuma|cumartesi|pazar|Pazartesi|Salı|Çarşamba|Perşembe|Cuma|Cumartesi|Pazar|hafta|gün|Günler"

   cümleler = tokenize.sent_tokenize(self)
   for cümle in cümleler:
       hepsini_buldum = False
       while not hepsini_buldum:

           tarih = re.search(regex, cümle)
           if tarih:
               isaretlenmisTarihListesi.append(tarih.group())
               cümle = cümle[tarih.span()[1]:]
           else:
               hepsini_buldum = True

def saatBul(self):

    regex =r"\d{2}:\d{2}"

    cümleler = tokenize.sent_tokenize(self)
    for cümle in cümleler:
        hepsini_buldum = False
        while not hepsini_buldum:

            tarih = re.search(regex, cümle)
            if tarih:
                isaretlenmisTarihListesi.append(tarih.group())
                cümle = cümle[tarih.span()[1]:]
            else:
                hepsini_buldum = True

def gunayBul(self):
    aylar = "Ocak|ocak|Şubat|şubat|Mart|mart|nisan|Nisan|mayıs|Mayıs|Haziran|haziran|Temmuz|temmuz|Ağustos|ağustos|Eylül|eylül|Ekim|ekim|Kasım|kasım|aralık|Aralık"
    aylarRakamsal = "\d{2}"

    ayBul = aylar

    ayırıcı1 = "[\s]"


    ayırıcılar =  ayırıcı1

    gün1 = "\d{2}"
    gün2 = "\d{1}"

    günler = "(" + gün1 + "|" + gün2 + ")"

    yıl = "\d{4}"

    regex = ayırıcılar+günler + ayırıcılar + ayBul + ayırıcılar + "\D"

    cümleler = tokenize.sent_tokenize(self)
    for cümle in cümleler:
        hepsini_buldum = False
        while not hepsini_buldum:

            tarih = re.search(regex, cümle)
            if tarih:
                isaretlenmisTarihListesi.append(tarih.group())
                cümle = cümle[tarih.span()[1]:]
            else:
                hepsini_buldum = True

def tarihBul1(self):
    aylar = "Ocak|ocak|Şubat|şubat|Mart|mart|nisan|Nisan|mayıs|Mayıs|Haziran|haziran|Temmuz|temmuz|Ağustos|ağustos|Eylül|eylül|Ekim|ekim|Kasım|kasım|aralık|Aralık"
    aylarRakamsal = "\d{2}"

    ayBul = "(" + aylar + "|" + aylarRakamsal + ")"

    ayırıcı1 = "[\s]"
    ayırıcı2 = "[\-]"
    ayırıcı3 = "[\/]"

    ayırıcılar = "(" + ayırıcı1 + "|" + ayırıcı2 + "|" + ayırıcı3 + ")"

    gün1 = "\d{2}"
    gün2 = "\d{1}"

    günler = "(" + gün1 + "|" + gün2 + ")"

    yıl = "\d{4}"

    regex = yıl + ayırıcılar + yıl

    cümleler = tokenize.sent_tokenize(self)
    for cümle in cümleler:
        hepsini_buldum = False
        while not hepsini_buldum:

            tarih = re.search(regex, cümle)
            if tarih:
                isaretlenmisTarihListesi.append(tarih.group())
                cümle = cümle[tarih.span()[1]:]
            else:
                hepsini_buldum = True

tarihBul(paragraf)
anahtarBul(paragraf)
saatBul(paragraf)
gunayBul(paragraf)
tarihBul1(paragraf)

print("Tarih işaretlemesi tamamlandı.")
print(len(isaretlenmisTarihListesi))

etiketlenmisText = paragraf
print("Derlem etiketleniyor...")
isaretlenenYerIsimleri = list(dict.fromkeys(isaretlenenYerIsimleri))
isaretlenmisParaListesi = list(dict.fromkeys(isaretlenmisParaListesi))
isaretliKisiListesi = list(dict.fromkeys(isaretliKisiListesi))
isaretlenenKurumListesi = list(dict.fromkeys(isaretlenenKurumListesi))
isaretlenmisTarihListesi = list(dict.fromkeys(isaretlenmisTarihListesi))


for i in range(len(isaretliKisiListesi)):
    etiketlenmisText = etiketlenmisText.replace(f'{isaretliKisiListesi[i]}',
                                                f'<b_enamex TYPE="PERSON">{isaretliKisiListesi[i]}<e_enamex>')
for i in range(len(isaretlenenYerIsimleri)):
    isaretlenenYerIsimleri[i] = isaretlenenYerIsimleri[i].strip()
    if isaretlenenYerIsimleri[i] in etiketlenmisText:
        index = etiketlenmisText.index(isaretlenenYerIsimleri[i])
        if etiketlenmisText[index - 1] != ">":
            etiketlenmisText = etiketlenmisText.replace(f'{isaretlenenYerIsimleri[i]}',
                                                        f'<b_enamex TYPE="LOCATION">{isaretlenenYerIsimleri[i]}<e_enamex>')

for i in range(len(isaretlenmisParaListesi)):
    etiketlenmisText = etiketlenmisText.replace(f'{isaretlenmisParaListesi[i]}',
                                                f'<b_numex TYPE="MONEY">{isaretlenmisParaListesi[i]}<e_numex>')

for i in range(len(isaretlenmisTarihListesi)):
    etiketlenmisText = etiketlenmisText.replace(f'{isaretlenmisTarihListesi[i]}',
                                                f'<b_numex TYPE="DATE">{isaretlenmisTarihListesi[i]}<e_numex>')

for i in range(len(isaretlenenKurumListesi)):
    etiketlenmisText = etiketlenmisText.replace(f'{isaretlenenKurumListesi[i]}',
                                                f'<b_enamex TYPE="ORGANIZATION">{isaretlenenKurumListesi[i]}<e_enamex>')

file = open('etiketliText.txt', 'w', encoding='utf-8')
file.write(etiketlenmisText)
file.close()
print("İşlem tamamlandı. etiketliText.txt dosyasından etiketli dosyaya erişilebilir.")

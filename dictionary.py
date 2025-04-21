# andmed={}
# andmed = {'nimi': 'Mari', 'vanus': 25, 'keel': 'eesti'}
# andmed = dict(nimi='Mari', vanus=25, keel='eesti')
# print(andmed)
# print(andmed['nimi'])
# print(andmed.get('nimi'))
# print(andmed.get('aadress', 'Ei ole määratud'))
# print(andmed.keys())
# print(andmed.values())
# for k,v in andmed.items():
#     print(k,v)
# andmed['email']="email@email.com"
# andmed["prillid"]=True
# print(andmed)
# del andmed["prillid"]
# print(andmed)
# andmed.pop("email")
# print(andmed)
# andmed.update({"nimi":"Kati"})
# print(andmed)



from random import *
from xml.dom.expatbuilder import ParseEscape
from sõnastik import *


# read = ['Mis on Python?:programmeerimiskeel', 'Eesti pealinn?:Tallinn', "Leedu pealinn?:Vilnus"]
# kus_vas = {}
# for rida in read:
#     kysimus, vastus = rida.split(':')
#     kus_vas[kysimus.strip()] = vastus.strip()
# print(kus_vas)

# küsimused=list(kus_vas.keys())
# while True:
#     n=randint(0, len(read)-1)
#     valitud_küsimus=küsimused[n]
#     print(valitud_küsimus)
#     vastus=input("Sisesta vastus: ")
#     if kus_vas[valitud_küsimus].lower()==vastus.lower():
#         print("Õige vastus")
#         break
#     else:
#         print("Vale vastus")




print("Welcome to the one and only estonian-russian-english dictionary!")
print()

while True:
    print("""

    1. loob kolme keele sõnastiku

    2. otsib sõna mistahes keelest ja kuvab teised tõlked

    3. lisab uue sõna kolme keelde

    4. parandab olemasoleva sõna

    5. kuvab kogu sõnastiku

    6. küsib kasutajalt, millisest keelest millisesse ta soovib tõlkida

    7. teadmiste kontroll juhuslike sõnadega

    8. kuvab testi lõpptulemuse

    9. küsib sisendi ja kontrollib tühjust

    10. ütleb sõna kõva häälega

    11.  exit

    
 """)
    vastus=int(input())
    if vastus==1:
        sõnastik=create_3_lang_dict()
    elif vastus==2:
             search_for_a_word(sõnastik)
    elif vastus==3:
        add_word(sõnastik)
    elif vastus==4:
        4
    elif vastus==5:
        print(sõnastik)
    elif vastus==6:
        translate(sõnastik)
    elif vastus==7:
        score=test(sõnastik)
    elif vastus==8:
        print(f"Score {score}")
    elif vastus==9:
        9
    elif vastus==10:
        10
    elif vastus==11:
        
    
        print("Nägemist")
        break

# est = ['koer', 'kass', 'maja', 'auto', 'päike']
# rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
# eng = ['dog', 'cat', 'house', 'car', 'sun']
# sõnastik = []
# for e, r, g in zip(est, rus, eng):
#     sõnastik.append({'est': e, 'rus': r, 'eng': g})
# # print(sõnastik)
# # print(sõnastik[3]["rus"])
# # print(len(sõnastik))
# # for e in sõnastik:
# #     print(e.values())

# #     listik=list(e)
# #     print(listik)
# word=input("Input a word of interest ")
# lang=input("Language in which the word is searched. est/eng/rus ")
# if word.isalpha():
    

#         for e in sõnastik:
           
            
#             if word in e[lang]:
#                 print(e)
                
#                 break
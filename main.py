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

from sõnastik import *


# # read = ['Mis on Python?:programmeerimiskeel', 'Eesti pealinn?:Tallinn', "Leedu pealinn?:Vilnus"]
# # kus_vas = {}
# # for rida in read:
# #     kysimus, vastus = rida.split(':')
# #     kus_vas[kysimus.strip()] = vastus.strip()
# # print(kus_vas)

# # küsimused=list(kus_vas.keys())
# # while True:
# #     n=randint(0, len(read)-1)
# #     valitud_küsimus=küsimused[n]
# #     print(valitud_küsimus)
# #     vastus=input("Sisesta vastus: ")
# #     if kus_vas[valitud_küsimus].lower()==vastus.lower():
# #         print("Õige vastus")
# #         break
# #     else:
# #         print("Vale vastus")





hello()
while True:
    print("Main menu")
    print()
    print("""

    1. Create a three language dictionary

    2. Search for a word in created dictionary

    3. Add a word and its translations to the dictionary

    4. Corrects an exicting word

    5. Shows the entire dictionary 

    6. Translate a word

    7. A test of knowledge

    8. Test result

    9. Write anything

    10. Spells a word

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
        correct_word(sõnastik)
    elif vastus==5:
        print(sõnastik)
    elif vastus==6:
        translate(sõnastik)
    elif vastus==7:
        score=test(sõnastik)
    elif vastus==8:
        print(f"Score {score}")
    elif vastus==9:
        kysi_kasutajalt_sisestus()
    elif vastus==10:
        raagi(input("Write a word to be spelled: "))
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


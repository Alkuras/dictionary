
import json
import ast 
  
from random import randint


import pyttsx3
def ast_read():
    jarjend=[]
    with open('sõnastik.txt',encoding="utf8") as f: 
        data = f.read() 
        o=ast.literal_eval(data)
        for rida in f:
            rida=ast.literal_eval(rida)
            jarjend.append((rida.strip()))
    return jarjend

def find(user_input):
    for item in "dictionary.json":
        if item["eng"] == user_input:
            return item["id"]

def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf8")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf8")
    for line in jarjend:
        f.write(str(line)+"\n")
    f.close()

def writefile(fail:str,d:list):
    with open(fail, 'w',encoding="utf8") as f:
        json.dump(d, f)

# def create_3_lang_dict()->list:
#     """Creates basic 3 language dictionary"""

#     est = ['koer', 'kass', 'maja', 'auto', 'päike']
#     rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
#     eng = ['dog', 'cat', 'house', 'car', 'sun']
#     sõnastik = []
#     for e, r, g in zip(est, rus, eng):
#         sõnastik.append({'est': e, 'rus': r, 'eng': g})
#     writefile("dictionary.json",sõnastik)
    
#     print("Creation completed!")
#     return sõnastik





def create_3_lang_dict()->list:
    """Creates basic 3 language dictionary"""

    est = ['koer', 'kass', 'maja', 'auto', 'päike']
    rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
    eng = ['dog', 'cat', 'house', 'car', 'sun']
    sõnastik = []
    for e, r, g in zip(est, rus, eng):
        sõnastik.append({'est': e, 'rus': r, 'eng': g})
        
    print("Creation completed!")
    return sõnastik

def search_for_a_word(dictionary:list):
    """Searches in the dictionary for a specific word
    :dictionary:list: created by "create_3_lang_dict" function
    """
    word=input("Input a word of interest ")
    
    if word.isalpha():
        lang=input("Language in which the word is searched. est/eng/rus ")
        if lang=="est" or "rus" or "eng":
            for e in dictionary:

              if word.lower() in e[lang]:
                print(e)
                break   
        else:
            print("Choose the right language")
    else:
        print("Write a word")

# def search_for_a_word():
#     """Searches in the dictionary for a specific word
#     :dictionary:list: created by "create_3_lang_dict" function
#     """
#     word=input("Input a word of interest ")
    
#     if word.isalpha():
#         lang=input("Language in which the word is searched. est 0/eng 1/rus 2 ")
#         p=json.loads("dictionary.json")
#         if lang=="est" or "rus" or "eng":
#             for e in p:

#               if word.lower() in e[lang]:
#                 print(e)
#                 break   
#         else:
#             print("Choose the right language")
#     else:
#         print("Write a word")
             

def add_word(dictionary):
    """Adds a word to a dictionary created by "create_3_lang_dict" """

    print("Adding a new word to the dictionary!")
    while True:
        try:
            uus_est = input("Type the word in estonian: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    while True:
        try:
            uus_rus = input("Type the word in russian: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    while True:
        try:
            uus_eng = input("Type the word in english: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    dictionary.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
    print("New word is added!")

def correct_word(dictionary):
    """Corrects word in dictionary"""
    o=0
    for e in dictionary:
        o=str(o)
        print(o+"."+" ",end=" ")
        print(e)
        o=int(o)
        o+=1
    print()
    v=int(input("Write the number of correctable word: "))
    while True:
        try:
            uus_est = input("Type the word in estonian: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    while True:
        try:
            uus_rus = input("Type the word in russian: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    
    while True:
        try:
            uus_eng = input("Type the word in english: ").strip().lower()
            if uus_est.isalpha():
                break
            else:
                print("Write a word")
        except:
            print("ERROR")
    dictionary.insert(v,{'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})

def translate(dictionary):
    """Gives a choise from which language to which lanhuage translate"""

    f=input("Choose a language from translate: est/eng/rus")
    t=input("Choose a language to translate: est/eng/rus")
    if t=="est" or "rus" or "eng"and f=="est" or "rus" or "eng" :
        for e in dictionary:
            print(e[f])
            print(e[t])
    else:
        print("Choose the right language")

def test(dictionary)->int:
    """Starts a test and gives result"""
    t=input("Choose a language to translate words in test: est/eng/rus ")
    f=input("Choose a language to translate words in test to: est/eng/rus ")
    score=0
    if t=="est" or "rus" or "eng"and f=="est" or "rus" or "eng" :
        for e in dictionary:
      
          print(e[t]+f" in {f}")
          vastus=input("Answer: ")
          if vastus==e[f]:
              print("Right!")
              score+=1
          else:
              print("Wrong!")
        print(f"Score: {score}")
    else:
        print("Choose the right language")
    return score

def kysi_kasutajalt_sisestus():
    """"""
    while True:
        try:    
            anything=input("Type in anything: ")
            if len(anything)>0 and not " ":
                print("Sucsess!")
                break
            else:
                print("Failure, you're failure")
        except:
            print("ERROR")

# def raagii(tekst, keel='et'):
#     """"""
#     obj = gTTS(text=tekst, lang=keel, slow=False)
#     failinimi = "heli.mp3"
#     obj.save(failinimi)
#     playsound(failinimi)
def raagi(tekst):
    """Spells text"""
    if tekst.isalpha():
        mootor = pyttsx3.init()
        mootor.say(tekst)
        mootor.runAndWait()

def hello():
    """Greets the user"""
    greet="Welcome, dear user"
    print(greet)
    raagi(greet)

def save(sõnastik:list):
    """"""
    Kirjuta_failisse("sõnastik.txt",sõnastik)
    print("Saved")

def impor()->list:
    """"""
    Loe_failist("sõnastik.txt")
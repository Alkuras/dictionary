from random import randint


def create_3_lang_dict()->list:
    """Creates basic 3 language dictionary"""

    est = ['koer', 'kass', 'maja', 'auto', 'päike']
    rus = ['собака', 'кошка', 'дом', 'машина', 'солнце']
    eng = ['dog', 'cat', 'house', 'car', 'sun']
    sõnastik = []
    for e, r, g in zip(est, rus, eng):
        sõnastik.append({'est': e, 'rus': r, 'eng': g})
    return sõnastik

def search_for_a_word(dictionary:list):
    """Searches in the dictionary for a specific word
    :dictionary:list: created by "create_3_lang_dict" function
    """
    word=input("Input a word of interest ")
    lang=input("Language in which the word is searched. est/eng/rus ")
    if word.isalpha():

        for e in dictionary:
            
            if word.lower() in e[lang]:
                print(e)
                
                break

def add_word(dictionary):
    """Adds a word to a dictionary created by "create_3_lang_dict" """

    print("Adding a new word to the dictionary!")
    uus_est = input("Type the word in estonian: ").strip().lower()
    uus_rus = input("Type the word in russian: ").strip().lower()
    uus_eng = input("Type the word in english: ").strip().lower()
    
    dictionary.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
    print("Uus sõna on lisatud!")

def correct_word(dictionary):
    """Corrects word in dictionary"""
    o=0
    for e in dictionary:
        print(o+"."+" "+e)
        o+=1
    print()
    v=int(input("Write the number of correctable word: "))
    uus_est = input("Type the word in estonian: ").strip().lower()
    uus_rus = input("Type the word in russian: ").strip().lower()
    uus_eng = input("Type the word in english: ").strip().lower()
    dictionary.insert(v,{'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})

def translate(dictionary):
    """Gives a choise from which language to which lanhuage translate"""

    f=input("Choose a language from translate: est/eng/rus")
    t=input("Choose a language to translate: est/eng/rus")
    for e in dictionary:
      print(e[f])
      print(e[t])

def test(dictionary)->int:
    """Starts a test and gives result"""
    t=input("Choose a language to translate words in test: est/eng/rus ")
    f=input("Choose a language to translate words in test to: est/eng/rus ")
    score=0
    for e in dictionary:
      
      print(e[t]+f" in {f}")
      vastus=input("Answer: ")
      if vastus==e[f]:
          print("Right!")
          score+=1
      else:
          print("Wrong!")
    print(f"Score: {score}")
    return score

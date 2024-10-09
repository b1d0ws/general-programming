import string
from time import sleep

dic = list(string.ascii_uppercase)

def key_verify():
  while True: 
    key = input("Insira a chave a ser usada: ")
    try: 
      key = int(key)
      if 0 <= key <= 26:  
        print()
        print("Processando...")
        sleep(1)
        return key
      print("Insira um número entre 0 e 26")
    except:
      print("Somente números inteiros podem ser usados!")
      pass

def text_verify():
  text = input("Insira o texto a ser [de]codificado (sem acentos): ").upper()
  while True:
    if text.replace(" ","").isalpha():
      return text
    else:
      print("O texto só pode ter letras inclusas!")
      text = input("Insira o texto a ser codificado (sem acentos): ").upper()


def codify(text, key):
    codified_text = ""
    for letter in text:
        if letter == " ":
            codified_text += " "
        else:
            letter_position = dic.index(letter)
            new_position = letter_position + key
            if new_position < 25:
                codified_text += dic[new_position]
            else:
                new_position = new_position - 26
                codified_text += dic[new_position]
    return codified_text

def decodify(text, key, option="N"):
    decodified_text = ""

    if option == "S":
        sleep(1)
        print()
        for letter in text:
            if letter == " ":
                decodified_text += " "
            else:
                letter_position = dic.index(letter)
                new_position = letter_position - key
            if new_position >= 0:
                decodified_text += dic[new_position]
            else:
                new_position = new_position + 26
                decodified_text += dic[new_position]
    

    else:
        sleep(1)
        print()
        print("Listando possíveis respostas...")
        print("="*31)
        sleep(2)
        for key in range(26):
            decodified_text = ""
            print("CHAVE", key, "-", end=" ")

            for letter in text:
                if letter == " ":
                    decodified_text += " "
                else:
                    letter_position = dic.index(letter)
                    new_position = letter_position - key
                    if new_position >= 0:
                        decodified_text += dic[new_position]
                    else:
                        new_position = new_position + 26
                        decodified_text += dic[new_position]
            sleep(0.2)
            print(decodified_text)
        print("="*30)

    return decodified_text
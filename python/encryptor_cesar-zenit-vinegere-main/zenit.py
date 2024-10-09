from sys import exit
from time import sleep
import os

def zenit():
    while True:
        print()
        print("{:=^40}".format("ZENIT POLAR"))
        print(
            "\n"
            "[ 1 ] - Codificar/Decodificar\n"
            "[ 2 ] - Sobre a Cifra\n"
            "[ 3 ] - Voltar ao Menu\n"
            "[OUTRO] - Para Sair"
            "\n"
            )

        choice = input("Escolha a opção desejada: ")

        dic1 = ["Z", "E", "N", "I", "T"]
        dic2 = ["P", "O", "L", "A", "R"]

        if choice == "1":
            word = input("Insira a palavra a ser [de]codificada: (sem acentos): ").upper()
            codified_word = ""
            for i in word:
                if i in dic1:
                    i = dic2[dic1.index(i)]
                    
                elif i in dic2:
                    i = dic1[dic2.index(i)]
                
                codified_word += i

            print(codified_word)

        elif choice == "2":
            print('''
            Zenit Polar é uma sistema simples de criptografia[1], que consiste na substituição das letras de uma palavra pela sua 
            correspondente no nome ZENIT POLAR. As demais letras, que não compõem tais palavras, permanecem inalteradas, e ignoram-se os acentos   
            O Z substitui o P e vice e versa.
            O E substitui o O e vice e versa.
            O N substitui o L e vice e versa.
            O I substitui o A e vice e versa.
            O T substitui o R e vice e versa. 

            Nesse caso a codificação e decodificação ficam na mesma escolha, pois o mecanismo é o mesmo.
            '''
            )
            sleep(2)
            enter = input("Pressione ENTER para continuar...")
            os.system("cls")

        elif choice == "3":
            break

        else:
            print("Até mais ver =)")
            exit()
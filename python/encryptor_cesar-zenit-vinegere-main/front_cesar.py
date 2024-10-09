from time import sleep
from defs_cesar import key_verify, text_verify, codify, decodify
import os

def cesar():
    while True:
            print()
            print("{:=^40}".format("Cifra de César"))
            print(
                "\n"
                "[ 1 ] - Codificar\n"
                "[ 2 ] - Decodificar\n"
                "[ 3 ] - Sobre a Cifra\n"
                "[ 4 ] - Voltar ao Menu\n"
                "[OUTRO] - Sair"
                "\n"
                )

            choice = input("Escolha a opção desejada: ")

            if choice == '1':
                text = text_verify()
                key = key_verify()
                codified_text = codify(text, key) 
                print("A frase", text, "criptograda com a chave", key, "fica", codified_text)
                sleep(2)
                enter = input("Pressione ENTER para continuar...")
                os.system("cls")

            elif choice == '2':
                text = text_verify()
                option = input("Você tem a chave para decifrar? s/N ").upper()
                if option == "S":
                    key = key_verify()
                    decodified_text = decodify(text,key,option)
                    print("A frase", text, "descriptograda com a chave", key, "fica", decodified_text)
                    sleep(2)
                    enter = input("Pressione ENTER para continuar...")
                    os.system("cls")
                else:
                    decodify(text, 0)
                    sleep(2)
                    enter = input("Pressione ENTER para continuar...")
                    os.system("cls")

            elif choice == "3":
                print('''
                    Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, 
                    é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de cifra de substituição na qual cada 
                    letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. 
                    Por exemplo, com uma troca de três posições, A seria substituído por D, B se tornaria E, e assim por diante. 
                    O nome do método é em homenagem a Júlio César, que o usou para se comunicar com os seus generais.
        ''')
                sleep(2)
                enter = input("Pressione ENTER para continuar...")
                os.system("cls")

            elif choice == "4":
                break

            else:
                print("Até mais ver =)")
                exit()
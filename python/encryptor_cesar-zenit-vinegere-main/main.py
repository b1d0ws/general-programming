from time import sleep
from front_cesar import cesar
from zenit import zenit
from vinegere import vinegere
import os

while True:
    print("{:=^40}".format("Bem-Vindo ao Cifrador"))
    print(
        "\n"
        "[ 1 ] - Cifra de César\n"
        "[ 2 ] - Zenit Polar\n"
        "[ 3 ] - Cifra de Vinegère\n"
        "[OUTRO] - Para Sair"
        "\n"
        )
    choice_menu = input("Escolha a opção desejada: ")

    if choice_menu == '1':
        cesar()

    elif choice_menu == '2':
        zenit()

    elif choice_menu == '3':
        vinegere()

    else:
        print("Até mais ver =)")
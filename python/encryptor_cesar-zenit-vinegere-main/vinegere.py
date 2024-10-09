import string
from time import sleep
from os import system

#Dicionário que vai conter a matriz de Vinegère
dic = []

#Gerando as linhas e colunas da matriz
for i in range(26):
  dic_atual = []
  dic_atual = list(string.ascii_lowercase[i:] + string.ascii_lowercase[:i])
  dic.append(dic_atual)

#Dicionário auxiliar para enumerar as letras do alfabeto usando .index()
dic_auxiliar = list(string.ascii_lowercase)

#Modificando a chave para ter o tamanho da frase a ser traduzida
def generate_key(key, word):
    while len(key) < len(word):
        key += key
        #Se a chave ultrapassar o tamanho da palavra, reduzir a quantia de letras até ficar do tamanho certo
        while len(key) > len(word):
            key = key[:-1]
    return key

def vinegere():
    while True:
            print()
            print("{:=^40}".format("Cifra de Vinegère"))
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
            if choice == "1":
                word = input("Escolha a frase a ser codificada: ")
                key = input("Insira a chave a ser usada: ")
                key = generate_key(key, word)
                
                encrypted_word = ""
                for x in range(len(word)):
                  linha = dic_auxiliar.index(key[x])
                  coluna = dic_auxiliar.index(word[x])                
                  encrypted_word += dic[linha][coluna]
                
                print("Criptogrando", word, "com a chave", key)
                sleep(2)
                print("RESULTADO:", encrypted_word)
                sleep(2)
                enter = input("Pressione ENTER para continuar...")
                system("cls")

            elif choice == "2":
              word = input("Escolha a frase a ser decodificada: ").lower()
              key = input("Insira a chave a ser usada: ").lower()
              key = generate_key(key, word)
              
              decrypted_word = ""
              for x in range(len(word)):
                linha = dic_auxiliar.index(key[x])
                coluna = dic[linha].index(word[x])
                decrypted_word += dic_auxiliar[coluna]
                
              print("A frase final fica:", decrypted_word)

            elif choice == "3":
               print('''
            Numa cifra de César, cada letra do alfabeto é deslocada da sua posição um número fixo de lugares; por exemplo, 
            se tiver um deslocamento de 3, "A" torna-se "D", "B" fica "E", etc. A cifra de Vigenère consiste no uso de várias 
            cifras de César em sequência, com diferentes valores de deslocamento ditados por uma "palavra-chave".

            Para cifrar, é usada uma tabela de alfabetos que consiste no alfabeto escrito 26 vezes em diferentes linhas, cada 
            um deslocado ciclicamente do anterior por uma posição. As 26 linhas correspondem às 26 possíveis cifras de César. 
            Uma palavra é escolhida como "palavra-chave", e cada letra desta palavra vai indicar a linha a ser utilizada para 
            cifrar ou decifrar uma letra da mensagem. 
            '''
            )
               sleep(2)
               enter = input("Pressione ENTER para continuar...")
               system("cls")

            elif choice == "4":
              break

            else:
              print("Até mais ver =)")
              exit()
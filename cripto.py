from os import system, name
from time import sleep
import json
import ast
import string
import random

senhas = './cripto.json'

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = ['=', '4', 't', 'p', 'q', 'I', '2', 'H', '*', 'B', 'k', 'n', 'A', 'K', ']', '$', '+', 'a', '}', 'z', 'i', ',',
       'J', 'b', '<', '^', 'D', '!', '?', '>', '{', 'X', "'", '/', 'O', 'j', 'Z', '5', 's', 'r', 'f', '"', '\\', 'h',
       '0', 'c', '[', 'v', '(', 'M', '%', 'T', 'N', 'e', 'u', 'S', ')', '`', '#', ';', 'o', '|', '~', 'G', '.', 'Y',
       ' ', 'W', '_', 'Q', 'P', 'd', 'C', '-', '1', '9', 'E', 'V', 'R', '8', 'F', 'g', 'L', '3', 'm', 'U', '7', 'x',
       'w', '6', '&', '@', 'l', ':', 'y']

try:
    with open(senhas, 'r') as arquivo:
        encriptado = json.load(arquivo)
        dict_senhas = ""
        for letter in encriptado:
            index = key.index(letter)
            dict_senhas += chars[index]
        dict_senhas = ast.literal_eval(dict_senhas)
except FileNotFoundError:
    dict_senhas = {}


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def salvar_senha():
    texto_encript = ""
    dict_string = str(dict_senhas)
    for letter in dict_string:
        index = chars.index(letter)
        texto_encript += key[index]
    with open(senhas, 'w') as arquivo:
        json.dump(texto_encript, arquivo)


def criar_senha():
    nome_login = input("\nDe onde é esta senha?: ")
    login = input("Login: ")
    senha = input("Senha: ")
    dict_senhas[nome_login.upper()] = [login, senha]
    sleep(1)
    clear()


def exibir_senhas():
    print("\n****** Senhas ******")
    for i, logins in enumerate(dict_senhas, start=1):
        print(f"~~~~~~ {logins} ~~~~~~ \nlogin: {dict_senhas[logins][0]} \nsenha: {dict_senhas[logins][1]}")
    sleep(5)
    clear()


def excluir_senha():
    try:
        print("\n** Qual senha deseja excluir? **")
        for i, logins in enumerate(dict_senhas, start=1):
            print(f"-> {logins}")
        senha = str(input())
        dict_senhas.pop(senha.upper())
        print(f"Os dados de {senha.upper()} foram removidos!")
        sleep(2)
        clear()
    except:
        print("Valor inválido!")


while True:
    try:
        print("\n****** Opções ******  ")
        print("1. Adicionar Senha")
        print("2. Exibir Senhas")
        print("3. Remover Senha")
        print("4. Sair")
        escolha = int(input())

        if escolha == 1:
            clear()
            criar_senha()
            salvar_senha()
        elif escolha == 2:
            if dict_senhas == {}:
                print("\nVocê não possui senhas salvas!")
                sleep(1)
                clear()
            else:
                clear()
                exibir_senhas()
        elif escolha == 3:
            if dict_senhas == {}:
                print("\nVocê não possui senhas salvas!")
                sleep(1)
                clear()
            else:
                clear()
                excluir_senha()
                salvar_senha()
        elif escolha == 4:
            print("\nSaindo do programa. Até mais!")
            sleep(2)
            clear()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            clear()
    except:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        clear()
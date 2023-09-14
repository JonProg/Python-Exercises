import colorama
import os
from random import choice
from colorama import Back, Fore
from pyfiglet import figlet_format

colorama.init()
senhas = ['python','anime','java','curl']
senha = choice(senhas)
elements = ['*']*len(senha)
numero_tentativas = 0

print(Fore.LIGHTBLUE_EX + '-'*73)
print(Fore.LIGHTYELLOW_EX + figlet_format('Palavra Secreta', font="standard"))
print(Fore.LIGHTBLUE_EX + '-'*73)

while True:
    new_senha=''
    print(f'{Fore.LIGHTMAGENTA_EX}Digite uma letra:', end='')
    letra = input()

    if len(letra)>1 or len(letra)<1:
        print(f'{Fore.YELLOW}Digite apenas uma letra')
        continue

    numero_tentativas += 1

    if letra in senha:
        elements[senha.find(letra)] = letra

    for i in elements:
        new_senha += i
    
    print(f'{Fore.LIGHTCYAN_EX}Palavra formata:{new_senha}')
    
    if new_senha == senha:
        os.system('cls')
        print(f'{Fore.GREEN}{Back.BLACK}--|VOCÊ GANHOU PARABÉNS!!|--')
        print(f'{Fore.LIGHTMAGENTA_EX}{Back.BLACK}--A palavra era: {senha}')
        print(f'{Fore.LIGHTBLUE_EX}{Back.BLACK}--Tentativas: {numero_tentativas}')
        break
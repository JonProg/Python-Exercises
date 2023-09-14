
#---------------------------------------

#Importações necessárias

import colorama
from colorama import Back, Fore, Style
from math import sqrt
from pyfiglet import figlet_format

colorama.init(autoreset=True)
#---------------------------------------

#Gerador de IPV4

string = '012345678901234567890123456789012345678901234567890123456789'
list_string = '.'.join([string[i:i+10] for i in range(0,len(string),10)])
print(list_string)

#---------------------------------------

#Coverte número; Usando try e except com condicionais sendo {try = tenta} e {except = se não tenta isso}

print(Fore.MAGENTA + '-'*66)
print(Fore.LIGHTCYAN_EX + figlet_format("Raiz Quadrada", font="standard"))
print(Fore.MAGENTA + '-'*66)

def convert_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    print(Fore.LIGHTRED_EX + "BREAK -- B")
    numero = convert_numero(input("Digite um valor: "))
    if numero is None:
        print('Erro: O valor digitado não é um número')
        continue
    elif numero == 'B':
        break
    else:
        print(f'Raiz quadrada de {numero}: {round(sqrt(numero),2)}')
    
#---------------------------------------
        
#Decoradores; Servem para adicionar funções a uma função tipo uma {função 2.0}

def master(funcao):
    def slave(*args,**kwargs):
        print('Estou decorado')
        funcao(*args,**kwargs)
    return slave

@master #Um decorador que resumindo: Adiciona funções a uma outra função como um upgrade
def fala_oi():
    print('Oi')

fala_oi()

#---------------------------------------

#---Parâmetros mutáveis em funções---

def lista_de_cliente(clientes_iteravel,lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_cliente = ['Samuel']
clientes1= lista_de_cliente(['Jonas','Dandara','Gabriel'],lista_cliente)
clientes2= lista_de_cliente(['Marcos','Gustavo','Chriys'])

print(clientes1)
print(clientes2)

#---------------------------------------

#---Porcentagem---

print(Fore.MAGENTA + '-'*50)
print(Fore.LIGHTCYAN_EX + figlet_format('Porcentagem', font="standard"))
print(Fore.MAGENTA + '-'*50)

while True:
    print("BREAK -- [0]\n")
    aumenta_or_diminui = input("Você vai aumentar[+] ou diminuir[-] um valor? ")
    if aumenta_or_diminui not in '+-':
        print()
        print("Digite  + ou - \n|__(*0_0)__/")
        print()
        continue

    valor_product = float(input("Digite o valor do produto:"))

    if valor_product == 0:
        break

    porcent = int(input(f"Digite a porcentagem:"))
    
    add_sub = ''
    valor_new = int
    if aumenta_or_diminui.startswith('+'):
        add_sub = 'aumentado'
        valor_new = valor_product+((valor_product*porcent)/100)

    elif aumenta_or_diminui.startswith('-'):
        add_sub = 'diminuido'
        valor_new = valor_product-((valor_product*porcent)/100)
    

    print(f"O valor do produto foi {add_sub} em {porcent}% ficando: {valor_new} ")

#---------------------------------------

#--Desempacotamento em chamadas de funções--
pokemons = ['Chamander','Bulbasauro','Squirtle','Kadabra','Pikachu']
print(*pokemons, sep='\n,--')

#---------------------------------------

















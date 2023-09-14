import colorama
import os
from colorama import Fore
from pyfiglet import figlet_format

colorama.init(autoreset=True)
lista_items = []
#---------------------------------

print(Fore.LIGHTBLUE_EX + '-' * 80)
print(Fore.LIGHTYELLOW_EX + figlet_format('Lista de Compras', font="doom"))
print(Fore.LIGHTBLUE_EX + '-' * 80)

while True:
    bar = f'{Fore.YELLOW}|'
    print(Fore.MAGENTA + '-' * 25)
    print(f'{Fore.RED}--|{Fore.CYAN}Selecione uma opção{Fore.RED}|--')
    print(Fore.MAGENTA + '-' * 25)

    print(Fore.YELLOW + '-' * 31)
    print(f'{bar}{Fore.MAGENTA}[i]nserir{bar:>3}',end='')
    print(f'{bar}{Fore.LIGHTRED_EX}[a]pagar{bar:>3}',end='')
    print(f'{bar}{Fore.LIGHTGREEN_EX}[l]istar{bar:>3}:',end='')
    opcao = input().lower()
    os.system('cls')

    if opcao == 'a':
        apagar = int(input('Escolha o indice para apagar:'))
        try:
            lista_items.pop(apagar)
        except IndexError:
            print('Não foi possível apagar este índice')
        except ValueError:
            print('Por favor digite um número int.')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'i':
        valor = input('Valor:')
        lista_items.append(valor)

    elif opcao == 'l':
        if lista_items == []:
            print('Nada para listar')
        for i, item in enumerate(lista_items):
            print(i, item)
    else:
        print('Por favor, escolha i, a ou l.')

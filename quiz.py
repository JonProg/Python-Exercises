import colorama
from colorama import Fore
from pyfiglet import figlet_format

colorama.init()

print(Fore.YELLOW + figlet_format('Quiz', font='big'))
perguntas = [
    {
        'Pergunta':'Quanto é 8*9?',
        'Opções':['54','74','71','72'],
        'Resposta':'72',
    },
    {
        'Pergunta':'Quanto é 456+140?',
        'Opções':['590','596','595','600'],
        'Resposta':'596',
    },
    {
        'Pergunta':'Quanto é 64/2?',
        'Opções':['35','31','32','34'],
        'Resposta':'32',
    },
]
acertos = 0
for pergunta in perguntas:
    print(Fore.CYAN + 'Pergunta: '+pergunta['Pergunta'])
    for indice, opcao in enumerate(pergunta['Opções']):
        print(Fore.MAGENTA + f'{indice+1})', opcao)
    try:
        res = int(input('Escolha uma opção:'))
        if pergunta['Opções'][res-1] == pergunta['Resposta']:
            print(Fore.GREEN + '--Acertou!!--')
            acertos += 1
        else:
            print(Fore.RED + '--Errou!!--')
    except:
        print(Fore.RED + '--Errou!!--')
print(f'{Fore.GREEN}Você acertou {acertos}\n{Fore.LIGHTBLUE_EX}de {len(perguntas)} perguntas')
    


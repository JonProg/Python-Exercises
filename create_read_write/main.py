import json

#|--Criação de Arquivos em Python--|

"""Criando arquivos com Python + Context Manager with
 Usamos a função open para abrir
 um arquivo em Python (ele pode ou não existir)

 Modos:
 r (leitura), w (escrita), x (para criação)
 a (escreve ao final), b (binário)
 t (modo texto), + (leitura e escrita)
 Context manager - with (abre e fecha)

 Métodos úteis:
 write, read (escrever e ler)
 writelines (escrever várias linhas)
 seek (move o cursor)
 readline (ler linha)
 readlines (ler linhas)
 
 Vamos falar mais sobre o módulo os, mas:
 os.remove ou unlink - apaga o arquivo
 os.rename - troca o nome ou move o arquivo
 Vamos falar mais sobre o módulo json, mas:
 json.dump = Gera um arquivo json
 json.load """

pokedex={
    'Bulbasauro':{
        'TYPE':'(Grass)(Posion)',
        'HP': 45,
        'LV': 1,
    },
    'Charmander':{
        'TYPE':'(Fire)',
        'HP': 45,
        'LV': 1,
    },
    'Squirtle':{
        'TYPE':'(Water)',
        'HP': 45,
        'LV': 1,
    },
}

pokedex_json = json.dumps(pokedex, indent=True)

with open('poke.json','w+') as file:
    file.write(pokedex_json)

print('Este módulo se chama', __name__)

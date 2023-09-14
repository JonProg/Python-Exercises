import colorama
from itertools import groupby

colorama.init()
pokemons = [
    {'nome': 'Ceruledge', 'tipo':'Fire'},
    {'nome': 'Monferno', 'tipo':'Fire'},
    {'nome': 'Charmeleon', 'tipo':'Fire'},
    {'nome': 'Tangela', 'tipo':'Gram'},
    {'nome': 'Chikorita', 'tipo':'Gram'},
    {'nome': 'Snivy', 'tipo':'Gram'},
    {'nome': 'Squirtle', 'tipo':'Water'},
    {'nome': 'Psyduck', 'tipo':'Water'},
    {'nome': 'Kyogre', 'tipo':'Water'},
]

def ordena(pokemons):
    return pokemons['tipo']

pokemons_agrupados = sorted(pokemons, key=ordena)
grupos = groupby(pokemons_agrupados, key=ordena)

for tipo, grupo in grupos:
    print()
    print(f'|--{tipo}--|')
    for pokemon in grupo:
        print(pokemon)
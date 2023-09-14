from functools import partial
from functools import reduce

#------------------------------------

# |-- (map) para mapear dados --|

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1

)

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print_iter(novos_produtos)

#------------------------------------

#|--Filter--|

#--Na forma de list comprehension--

novos_produtos = [
     p for p in produtos
     if p['preco'] > 100
     ]

#--Na forma funcional filter()--

novos_produtos = filter(
    lambda produto: produto['preco'] > 100,
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)

#------------------------------------

#|--Reduce--|

total = reduce(
    lambda ac, p: ac + p['preco'],#Função que soma todos os preços retornando o ultimo valor a ser acumulado
    produtos,
    0 #Valor que o acumulador(ac) vai começar
)

print('Total é', total)

#------------------------------------




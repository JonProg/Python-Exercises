#---------------------------------

#|--Zip e Zip_Longest--|

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1, l2)))#Usa como referencia a menor lista

print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))#Usa como referencia a maior lista

#---------------------------------

#|--Somando Listas --|

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

#---------------------------------
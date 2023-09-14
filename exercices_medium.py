import sys
import copy

#---Funções---

#Argumentos posicionais func(1,2,3) | Argumentos nomeados func(a=1,b=2,c=3)

#---------------------------------
#Funçãoa para multiplicar valores

def multiplique(*args):
    total = 1
    for num in args:
        total*=num
    return total

print(multiplique(2,3,5))

#---------------------------------

#---Closure---

#Exercicio 1

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')#Aqui eu estou chamando a função criar_saudacao() sendo está estatica
s2 = criar_saudacao('Boa noite')

print(s1('Jonas'))#Já nesse ponto estou chamando a função saudar() que está sendo dinâmica
print(s2('Samuel'))

#--Continuação de Clasure--

#Exercicio 2

def somar(x, y):
    return x + y


def multiply(x, y):
    return x * y


def cria_funcao(funcao, x):
    def conta(y):
        return funcao(x,y)
    return conta


soma_com_cinco = cria_funcao(somar, 5)
multiplica_por_dez = cria_funcao(multiply, 10)

print(multiplica_por_dez(10))
#---------------------------------

#--Duplicar, Triplicar e Quadrublicar---

def multiplica(multi):
    def valor(numero):
        return f'Resultado:{int(numero*multi)}'
    return valor

duplica = multiplica(2)
triplica = multiplica(3)
quadruplica = multiplica(4)

print(quadruplica(5))

#---------------------------------

""" import copy
    copy.deepcopy(valor)
    --comando usado para fazer uma copia profunda--
    
    list ou dict.copy() é uma copia raza"""

#---------------------------------

#--Conjuntos--

""" s1 = set() --vazio
    s1 = {'Jonas',17} --com dados"""

""" Sets são eficientes para remover valores duplicados
    de iteráveis.
     - Seus valores serão sempre únicos;
     - Não aceitam valores mutáveis;
     - não tem índexes;
     - não garantem ordem;
     - são iteráveis (for, in, not in)
    
    Métodos úteis:
        add, update, clear, discard
    
    Operadores úteis:
        união | união (union) - Une
        intersecção & (intersection) - Itens presentes em ambos
        diferença - Itens presentes apenas no set da esquerda
        diferença simétrica ^ - Itens que não estão em ambos"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )
#---------------------------------

#--Lambda--

listas_dict = [
    {'nome':'jin_woo', 'poder':'sombras'},
    {'nome':'naruto', 'poder':'rasengan'},
    {'nome':'goku', 'poder':'ginki dama'},
    {'nome':'saitama', 'poder':'soco'},
]

listas_dict.sort(key = lambda item: item['nome'])

for item in listas_dict:
    print(item)

#args -- argumentos não nomeados
#kwargs -- argumentos nomeados

#---------------------------------

#--list comprehension--

lista_comprehension = [num for num in range(1,10)]

#---------------------------------

#--Mapeamento--

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**produto, 'preco': round(((10/100) * produto['preco'])+produto['preco'], 2)}
    for produto in copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key = lambda value: value['nome'], reverse=True)
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key = lambda value: value['preco'], reverse=True)

#Em um mapeamento a nova lista tem que conter a mesma quantidade de elementos da lista antiga
#Sorted gera uma nova lista ou dict a partir da original e sort manipula a lista original

#---------------------------------

#--dict_comprehension--

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print(dc)

#---------------------------------

""" isinstace(valor, tipo desejado) - para saber se o objeto é de determinado tipo
    se colocar dois tipos = isinstace(valor, (tipo1, tipo2))"""

#---------------------------------

#--Generator e Iterator--

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator1 = (n for n in range(1000000))

#Caso queria ver o comparativo de uso de memoria importe a bliblioteca sys |comando -- (import sys)|
print(sys.getsizeof(lista))
print(sys.getsizeof(generator1))

print(generator1)

# for n in generator:
#     print(n)

#---------------------------------

#--Generator functions--

def generator(n=0, maximum=10):
    while True:
        yield n #Faz uma pausa
        n += 1
        if n >= maximum:
            return
gen = generator(maximum=1000000)
for n in gen:
    print(n)

#---------------------------------

#--Yield from--
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')

def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen #Começa de onde parou o ultimo yield
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())

for numero in g1:
    print(numero)
print()

#---------------------------------

#--try e except--

try:
    a = 18
    b = 0
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

finally: #Sempre será executado 
    print('CONTINUAR')

#---------------------------------

#--Raise--

def nao_aceito_zero(d):
    """O raise é meio que um editor de erros 
       onde você pôde alterar a mensagem de erro"""

    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') 
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide('8', '0'))

#---------------------------------

#--Importações--
"""
    Todas as importações  dentro do seu programa devem estar relativas ao __main__
    e elas não vão funcionar nos outros modulos já que o main muda
"""

#---------------------------------

#--Variaveis Livre + nonlocal--

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final #Essa variavel não pertence a esse escopo
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

#---------------------------------

#|--Funções decoradoras e decoradores--|

"""Decorar = Adicionar / Remover/ Restringir / Alterar
   Funções decoradoras são funções que decoram outras funções.
   Decoradores são usados para fazer o Python
   usar as funções decoradoras em outras funções
   Decoradores são "Syntax Sugar" (Açúcar sintático)."""

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
print(invertida)

#---------------------------------

# |--Decoradores com parâmetros--|
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) #A ordem de aplicação dos decoradores e de baixo para cima
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)

#---------------------------------

#|--Exercício - Unir listas--|

capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

print(zipper(capitais, siglas))

#---------------------------------

#|--Fuções Recursivas--|

"""Funções recursivas e recursividade
 - funções que podem se chamar de volta
 - úteis p/ dividir problemas grandes em partes menores
 
 Toda função recursiva deve ter:
 - Um problema que possa ser dividido em partes menores
 - Um caso recursivo que resolve o pequeno problema
 - Um caso base que para a recursão"""

def recursiva(inicio=0, fim=4):
    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

#---------------------------------

# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def soma02(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma02(1, 2, c=3, nome='teste')

#---------------------------------








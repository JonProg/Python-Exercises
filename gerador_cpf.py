#Validador de CPF
import random

cpf=''
for _ in range(9):
    cpf += str(random.randint(0,9))
#---Primeiro Digito---
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in cpf:
    resultado_digito_1 += int(digito)*contador_regressivo_1
    contador_regressivo_1-=1

digito_1 = (resultado_digito_1*10)%11 if (resultado_digito_1*10)%11 <=9 else 0

#---Segundo Digito---

dez_digitos = cpf+str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito)*contador_regressivo_2
    contador_regressivo_2-=1

digito_2 = (resultado_digito_2*10)%11 if (resultado_digito_2*10)%11 <=9 else 0

new_cpf=f'{cpf}{digito_1}{digito_2}'

print(new_cpf)

#---------------------------------------
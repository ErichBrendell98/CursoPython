"""
Formatando valores com modificadores - Aula 50

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÙMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

print()

nome = 'Erich Brendell'
print(f'{nome:s}')

print()

num_1 = 1
print(f'{num_1:0>10}')
num_2 = 1150
print(f'{num_2:0>10}')      #Coloca os números a esquerda
print(f'{num_2:0<10}')      #Coloca os números a direita
print(f'{num_2:0^10}')      #Coloca os números no centro
print(f'{num_2:0>10.2f}')

print()

nome = 'Araújo Medeiros'
print(f'{nome:#^50}')

print()

nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

print()

nome = 'Erich'
sobrenome = 'Brendell'
nome_formatado = '{0:$^50}\n{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

print()

nome = 'Erich Brendell araújo medeiros'
print(f'{nome.ljust(20, "#")}\n{nome.lower()}\n{nome.upper()}\n{nome.title()}')
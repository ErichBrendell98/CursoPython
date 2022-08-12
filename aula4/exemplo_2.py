"""
Operadores Relacionais - AULA 4 Parte 2

== > >= < <= !=
"""

# print(2 == 2)
# print(2 == 2 == 3 == 4 == 2)

# num_1 = 2
# num_2 = '2'
# print(num_1, num_2)
# print(num_1 == num_2)

# expression = num_1 == num_2     #expression =  False or True (False)
# print(expression)

# num_3 = 3
# expression = num_1 <= num_3
# print(expression)

# var_1 = var_3 = 'Erich' 
# var_2 = 'Brendell'

# names = (var_1 != var_2)
# names2 = (var_1 == var_2)
# names3 = (var_1 == var_3)
# print(names, names2, names3)

nome = input('Nome: ')
idade = int(input('Idade: '))

## Limite para pegar empréstimo
idade_menor = 20    #muito jovem
idade_maior = 30    #muito velho


if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
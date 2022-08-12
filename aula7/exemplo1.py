"""
while em Python - Aula 7
utilizando para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""
# x = 0 # coluna

# while x < 5:
#     print(x)
#     x += 1
# print('Acabou!!!')

# while x < 10:
#     if x == 3:
#         x += 1
#         #continue # Pula pra o próximo laço
#         break
#     print(x)
#     x += 1 # essa linha é pulada e gera um laço infinito
# print('Acabou!!!')

# while x < 10:
#     y = 0 # linha
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#     x += 1  # x = x + 1
# print("It's Over")

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif  operador == '/':
        print(num_1 / num_2)
    elif  operador == '*':
        print(num_1 * num_2)
    else:
        print('operador inválido')
    
    sair = input('Deseja sair? [s]im ou [n]ão:')
    if sair in 'sS':
        break
    elif sair in 'nN':
        continue

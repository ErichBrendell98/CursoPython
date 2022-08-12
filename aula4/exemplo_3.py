"""
Operadores Lógicos - Aula 4 Parte 3
and, or, not
in e not in
"""
# (Verdadeiro E Verdadeiro) = Verdadeiro
#comp1 and comp2

# (Verdadeiro OU Verdadeiro) = Verdadeiro
#comp1 or comp2

# a = 2
# b = 3

# # Not
# if not b > a:
#     print('B é maior do que A')
# elif b == a:
#     print('B é igual à A')
# else:
#     print('A é maior do que B.')

# c = ''
# if not c:
#     c = int(input('c: '))
#     print(c)

# nome = 'Erich Brendell'

# if 'rendel' not in nome:
#     print('Executei')
# else:
#     print('Existe o texto')

user = input('Nome de usuário: ')
passwd = input('Senhda do usuário: ')

usuario_bd = 'erich'
senha_bd = '123456'

if usuario_bd == user and senha_bd == passwd:
    print('logado')
else:
    print('erro')
"""
Minijogo de adivinhação feito em python
"""

secreto = 'perfume'
digitadas = []
chances = 14

while True:
    if chances > 0:
        print(f'Você tem {chances} chances restando')
    else:
        print('Você PERDEUUUU!!!')
        break

    letra = input('\nDigite uma letra: ')

    if len(letra) > 1:
        print('EEERRG isso não vale, digite apenas uma letra.')
        continue
    
    digitadas.append(letra)

    if letra in secreto and letra != '':
        print(f'UHUUUULLL a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AAAAFFFF a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOUUUUU!!!\nA palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    chances -= 1
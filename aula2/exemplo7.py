"""
Variáveis:
    Variáveis são usadas para armazenar valores e dar um nome a um trecho de memória do computador onde os valores estão armazenados.txt

    Quando uma variável é criada, o Python já determina qual seu tipo baseando-se no seu valor. Isso se chama tipagem dinâmica.

    Nomes de variáveis devem iniciar com uma letra
    Nomes de variáveis podem conter números.
    Nomes compostos podem ser separados por um _
    Por conversão, utilize apenas letras minúsculas
"""

nome = 'Erich Brendell'       #string
idade = 24                  #int
altura = 1.82               #float
peso = 93                   #int
data_atual = '06/08/2022'   #string

#Fórmula IMC = peso dividido pelo quadrado da altura
indice_massa_corporal = peso/(altura**2)
#indice_massa_corporal = '{:.2f}'.format(indice_massa_corporal)

print(f'\nA variável nome recebeu: {nome}')
print(f'A variável idade recebeu: {idade}')
print(f'A variável data recebeu: {data_atual}')
print(f'\n{nome} tem {idade} anos e seu IMC é {indice_massa_corporal}')

#A função format é usada em strings para formatar o texto de maneira que a leitura e escrita fiquem mais fáceis.
print('\n{} tem {} anos e seu IMC é {}.'.format(nome, idade, indice_massa_corporal))

#Um outro exemplo ainda mais interessante é:
print(f'\n{nome} tem {idade} anos e seu IMC é {indice_massa_corporal:.2f}')

#Utilizando índices
print('\n{0}{0}{0}{0} tem {1} anos e seu IMC é {2}'.format(nome, idade, indice_massa_corporal))

mensagem = f'''
Um texto 
gigante
aqui
e agora eu vou
exibir minhas variáveis.
Variável nome = {nome}
Variável idade = {idade} 
'''
print(mensagem)

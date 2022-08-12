"""
Números int e float (-10, 0, 10, 20) e (-10.50, -1.0, 14.7, 2.5, 2.0)
Números inteiros (int) e números de ponto flutuante (float)
NÃO RECEBEM aspas, apenas se quisermos tratar números como texto (string)
Números de ponto flutuante (com decimais) usam ponto para separação das casas
O operador + serve tanto para soma quanto concatenação
"""

#Exemplo de números sem aspas
print(f'A soma de 5+5 é: {5+5}')                #Soma | Exibe: 10
print('Número tratado como texto:', '5' + '5')  #Concatena | Exibe: 55
print(f'-5.55*2 = {-5.55*2}')                   #Multipliação | Exibe: -11.1
print('-5.55'*2)                                #Repetição | Exibe: -5.55-5.55

"""
Operadores aritméticos
Os operadores aritméticos no Python são:
    +   sinal de mais           Adição/Concatenação
    -   sinal de menos          Subtração
    *   asterisco               Multiplicação/Repetição
    /   barra                   Divisão
    //  duas barras             Divisão com resultado inteiro
    %   porcentagem             Módulo (resto da divisão)
    **  dois asteriscos         Exponenciação ou potenciação
    ()  parênteses              Prioridade na  operação

    As operações de mesma prioridade são realizadas da esquerda para direita, com os () alterando a prioridade.
"""
print(f'Soma 2 com 2: {2+2}')                           #4
print(f'Concatena 2 com 2: {"2" + "2"}')                #22
print(f'Multiplica 2 com 2: {2*2}')                     #4
print(f'Repete "A" 5 vezes: {"A"*5}')                   #AAAAA
print(f'Divide 10 com 3: {10/3}')                       #3.333333333... 
print(f'Divide 10 com 3 (valor inteiro): {10//3}')      #3
print(f'Divide 10 com 3 (valor inteiro): {10/3:.0f}')   #3
print(f'Resto da divisão entre 10 e 3: {10%3}')         #1
print(f'2 elevado a 3: {2**3}')                         #8
print(f'Alterando a prioridade: {(5+2)*10}')            #70              

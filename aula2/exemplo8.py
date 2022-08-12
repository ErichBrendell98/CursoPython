"""
Introdução aos tipos de dados
int - números inteiros (positivos, negativos e zero)
float - números reais, com ponto (positivos ou negativos)
bool - valor lógico (booleano) - True == Verdadeiro, False == Falso
str - String ou cadeia de caracteres (texto)

Existem mais tipos de dados

Tudo em Python é um objeto, incluindo os tipos primitivos

Só é possível usar o operador de + com valores de mesmo tipos
Para concatenar valores de tipos diferentes, é necessário fazer um cast (conversão de valores) dos valores
É possível realizar operações aritméticas entre int e float
"""
inteiro = 5         #int
real = 6.2          #float
booleano = True     #bool
texto = '9.3'       #str
texto1 = 'Texto'    #str

print(inteiro + real)
#print(inteiro + texto) -> Não pode
print(inteiro + float(texto))

## Cast (convertendo string em float)
texto_float = float(texto)
print(texto_float + real)

#print(type(texto), type(texto_float))

##Não é permitido fazer
#print(int(texto))
#print(int(float(texto)))
#print(int(float(texto1)))

# Valores lógicos (bool), geralmente são usados em comparações
expressao = inteiro >= real #False
print(expressao)

# Use a função type(nome variavel), para saber seu tipo
# É possível converter qualquer tipo primitivo em string
# cast para string
print(f'O tipo da variável inteiro é: {type(inteiro)}')     #int
inteiro = str(inteiro)      #str
print(f'O tipo da variável inteiro agora é: {type(inteiro)}')   #str

print(f'O tipo da variável real é: {type(real)}')     #float
real = str(real)      #str
print(f'O tipo da variável real agora é: {type(real)}')   #str

print(f'O tipo da variável booleano é: {type(booleano)}')     #bool
booleano = str(booleano)      #str
print(f'O tipo da variável inteiro agora é: {type(booleano)}')   #str
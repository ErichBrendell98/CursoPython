"""
Listas em Python:
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#listaExemplo = [1, 2, 3, 4, 'Erich Brendell', True, 10.5]

#         0    1     2    3    4    5
#        -6   -5    -4   -3   -2   -1
lista = ['A', 'Bb', 'C', 'D', 'E', 10.5]
string = 'ABCDE'
print(string[1])    #B
print(lista[1])     #Bb
print(lista[-1])    #10.5
print(lista[5])     #10.5
print(lista)

lista[5] = 'Qualquer outra coisa'   #['A', 'Bb', 'C', 'D', 'E', 'Qualquer outra coisa']
print(lista[5])     #Qualquer outra coisa

##Fatiamento de lista
print(lista[0:3])   #['A', 'Bb', 'C']
print(lista[1:4])   #['Bb', 'C', 'D']
print(lista[:3])    #['A', 'Bb', 'C']
print(lista[2:])    #['C', 'D', 'E', 'Qualquer outra coisa']
print(lista[::2])   #['A', 'C', 'E']
print(lista[::-1])  #['Qualquer outra coisa', 'E', 'D', 'C', 'Bb', 'A']
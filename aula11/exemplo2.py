l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2))
print(min(l2))

l2 = range(1, 10)
print(l2)   #apenas com range retorna um obj 

l2 = list(range(0, 10))     #tornou o obj do tipo range, um iteravel do tipo list
print(l2)

soma = 0
for value in l2:
    soma += value
print(soma)


l3 = ['String', True, 10, -20.5]
for elem in l3:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}')
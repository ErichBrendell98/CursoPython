#operador: +
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2    #concatenação dos valores de l1 e l2
print(f'{l1}\n{l2}\n{l3}')  #l3 = l1 + l2

#extend
l1.extend(l2)   #l1 = [1, 2, 3] | l1 = [1, 2, 3, 4, 5, 6]
print(l1)
l1.extend('a')  #l1 = [1, 2, 3, 4, 5, 6, 'a']
print(l1)

#append
l2.append('b')  #l2 = [4, 5, 6] | l2 = [4, 5, 6, 'b']
print(l2)

#insert
l2.insert(0, 'banana')  #l2 = [4, 5, 6, 'b'] | l2 = ['banana', 4, 5, 6, 'b']
print(l2)

#pop
l2.pop()    #l2 = ['banana', 4, 5, 6, 'b'] | l2 = ['banana', 4, 5, 6]
print(l2)

##nova lista

#del
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l4)
l4.insert(0, 'Banana')
print(l4)
del(l4[0])
print(l4)
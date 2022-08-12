"""
For in em Python
Iterando strings com for
Função range(start = 0, stop, step=1)
"""

texto = 'Python'

for letra in texto:
    print(letra)

print()

for n in range(10):
    print(n)

print()

for n in range(5, 10):
    print(n)

print()

for n in range(0, 10, 2):
    print(n)

print()    

for n in range(20, 10, -1):
    print(n)

print()

for n in range(0, 100, 8):
    print(n)

print()

for n in range(100):
    if n % 8 == 0:
        print(n)
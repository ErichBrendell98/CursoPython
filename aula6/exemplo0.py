"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
    https://docs.python.org/3/library/stdtypes.html (tipos built-in)
    https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos     [012345678]
texto         = 'Python_s2'
# negativos    -[987654321]
print(texto[::-1])

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[:6]
nova_string2 = texto[-9:-3]
print(nova_string,'-', nova_string2, '-', texto[:-1])
print(texto[::3])

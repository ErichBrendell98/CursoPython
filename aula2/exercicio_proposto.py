"""
Crie 5 variáveis referentes aos dados de uma pessoa
Variáveis: nome, sobrenome, idade, altura e peso

Exiba uma apresentação de pessoa da seguinte forma:

Este é o(a) #nome #sobrenome. Ela/Ela nasceu em #ano_nascimento e tem #idade anos. #nome #sobrenome tem #altura de altura e pesa #peso kilos
"""

nome = 'Erich Brendell'
sobrenome = 'Araújo Medeiros'
idade = 24
altura = 1.82
peso = 93
ano_nascimento = 2022 - idade

print(f'Este é o {nome} {sobrenome}.\nEle nasceu em {ano_nascimento} e tem {idade} anos.\n{nome} {sobrenome} tem {altura} de altura e pesa {peso} kg')
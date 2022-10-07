# Operadores relacionais
# == > >= < <= !=

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)
#  Limite para pegar um empréstimo
idade_limite = 18


if idade >= idade_limite:
    print(f'{nome} PODE pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
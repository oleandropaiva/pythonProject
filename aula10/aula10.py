# Operadores relacionais
# == > >= < <= !=

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)
#  Limite para pegar um empréstimo
idade_menor = 20
idade_maior = 30


if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} PODE pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

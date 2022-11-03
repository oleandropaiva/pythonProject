"""
Operador ternário em Python
"""
idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Digite apenas números')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode acessar' if e_maior else 'Não pode acessar'

print(msg)

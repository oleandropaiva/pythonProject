"""
For / Else em Python
"""
variavel = ['Luiz Otávio', 'João', 'Maria']

for valor in variavel:
    if valor.lower().startswith('J'):
        break
    else:
        print('Não existe uma palavra que começa com J.')

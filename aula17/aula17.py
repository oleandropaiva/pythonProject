"""
while em Python
utilizadopara realizar ações emquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

x = 0  # coluna
while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x += 1  # x = x + 1

print('Acabou')




"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) :.2f
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d OU f)

> - Esquerda
< - Direita
^  - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao: .2f}')

#quando tenho uma string uso o (:s)

nome = 'Leandro Paiva'
print(f'{nome:s}')
print(f'{num_1:0>10}')
print(f'{num_2:0<10}')
print(f'{num_2:0^10}')



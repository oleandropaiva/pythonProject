"""
Desenpacotamento de listas em Python
"""
# atribui  n1      n2      n3
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 100]

n1, n2, n3, * outra_lista, ultimo_da_lista = lista

print(outra_lista)

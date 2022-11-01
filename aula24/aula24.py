"""
Desenpacotamento de listas em Python
"""
# atribui  n1      n2      n3
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4]

n1, n2, n3, * outra_lista = lista

print(n1, n2, n3, outra_lista)

"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
string = "O Brasil é o país país país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip())


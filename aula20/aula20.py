"""
For in em Python
Iterando strings com for

Função range(start=0, stop, step=1)range recebe 3 argumentos
"""
texto = 'Python'
nova_string = ''

# continue - pula para o próximo laço
# break  - termina o laço

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

    print(nova_string)

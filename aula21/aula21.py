"""
Listas em Python
fatiamento
append, insert, pop, clear, extend, +
min, max
range
"""
secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra"{letra}" Não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra
        else:
            secreto_temporario += '*'

    print(secreto_temporario)

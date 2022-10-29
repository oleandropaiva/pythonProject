variavel = ['Luiz Otávio', 'João', 'Maria']
for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)
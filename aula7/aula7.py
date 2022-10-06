nome = 'Leandro Paiva'  # string
idade = 37  # int
altura = 1.66  # int
e_maior = idade > 18  # boll
peso = 86
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))

print('{0} {0} {0} {1} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))

print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))




# print('Nome:', nome)  # string
# print('Idade:', idade)  # int
# print('Altura', altura)  # float
# print('É maior:', e_maior)  # boll


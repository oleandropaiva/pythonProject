usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Precisa digitar pelo menos 6 caracteres')
else:
    print('Cadastrado no sistema. ')


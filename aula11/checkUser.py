user = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Leandro'
senha_bd = '123456'

if usuario_bd == user and senha_bd == senha:
    print('Você está logado no sistema. 👏')
else:
    print('Usuário ou senha inválidos. 🤷‍♂️')
#        Índices
#        0123456789........33

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    print(nova_string)
    contador += 1

print(nova_string)

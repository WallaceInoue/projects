print('Digite idade da pessoa para entrer no cinema ')
print('Ao finalizar digite "sair"')
soma = 0
pessoa = 0
preco = 0


while True:
    idade = input('Digite sua idade: ')
    if (idade == 'sair'):
        break
    #pessoa += 1
    idade = int(idade)
    soma += idade
    if ( idade <= 3):
        preco += 0
        pessoa += 1


    elif (idade <= 12):
        preco += 15
        pessoa += 1

    elif (idade > 12):
        preco += 30
        pessoa += 1


media = soma / pessoa
print ('A media de idade é {} anos'.format(media))
print('valor total: {}'.format(preco))
print('total de pessoas: {}'.format(pessoa))


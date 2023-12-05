nome = input('Qual seu nome?')
if (nome.lower() == 'vinicius'):
    print('Ola, Vinicius !!!')
elif (nome.lower() != 'vinicius'):
    idade = int(input('Qual sua idade?'))
    if (idade < 18 ):
        print('Ola, {}, você tem {} anos MENOR de idade'.format(nome,idade))
    elif (idade > 100):
        print('Você digitou que tem {} provavel que nao existe'.format(idade))
    else:
        print('Ola, {} voce é MAIOR de idade'.format(nome))

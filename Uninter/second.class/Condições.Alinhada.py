print('-----MENU------')
print('Digite se deseja: \n'
      '1 - Maçã\n'
      '2 - Laranja \n'
      '3 - banana')
fruta = int(input('>>'))


if (fruta == 1):
    unidade = int(input('Quantas unidade você deseja:'))
    total = unidade * 2.30
    print('O valor total a pagar: R${}'.format(total))
elif (fruta == 2):
    unidade = int(input('Quantas unidade você deseja:'))
    total = unidade * 3.6
    print('O valor total a pagar: R${}'.format(total))
elif (fruta == 3):
    unidade = int(input('Quantas unidade você deseja:'))
    total = unidade * 1.85
    print('O valor total a pagar: R${}'.format(total))
else:
    print('Numero invalido!!!')
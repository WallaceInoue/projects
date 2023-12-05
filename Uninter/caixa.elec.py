valor = int(input('Digite um valor em R$: '))

while True:
    if (valor >= 100):
        ced1 = valor // 100
        valor = valor - ced1 * 100
        print('Cédulas de 100:{}'.format(ced1))
    if (valor >= 50):
       ced2 = valor // 50
       valor = valor - 50 * ced2
       print('Cédular de R$ 50:{}'.format(ced2))
    if (valor >= 20):
        ced3 = valor // 20
        valor -= 20 * ced3
        print('Cédular de R$ 20:{}'.format(ced3))
    if (valor >= 10):
        ced4 = valor // 10
        valor -= 10 * ced4
        print('Cédula de R$ 10: {}'.format(ced4))
    if (valor >= 5):
        ced = valor // 5
        valor -= ced * 5
        print('Cédulas de R$ 5 : {}'.format(ced))
    if(valor):
        print('Cédulas de R$ 1: {}'.format(valor))
        break
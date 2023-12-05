consumo = int(input('Quantidade de kWh consumida: '))
tipo = input('-----Digite o tipo de instalaçâo----- \n'
             'R = residencial\n'
             'I = industrial \n'
             'C = comercial \n'
             '>>')
if (tipo.lower() == 'r'):
    if (consumo <= 500):
        consumo *= 0.40
    elif (consumo > 500): ## ou else
        consumo *= 0.65
elif (tipo.lower() == 'i'):
    if (consumo <= 100):
        consumo *= 0.55
    elif(consumo > 1000):## ou else
        consumo *= 0.60
elif (tipo.lower() == 'c'):
    if (consumo <= 1000):
        consumo *= 0.55
    elif(consumo > 5000):## ou else
        consumo *= 0.60
else:
    print('INSTALAÇAO INVALIDA!!!')
print('O total de a pagar é de R${}'.format(consumo))


km = int(input('Quilometro percorrido (Km/h): '))
dia = int(input('Quantos dias foi alugado: '))

valor = dia * 60 + (km * 0.15)
print('O valor total pagar é de R${:.2f}'.format(valor))
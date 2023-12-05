game = {'nome':'Super Mario',
        'desenvolvedora':'nitendo',
        'ano':'1990'}
print(game)
print(game.values())
print(game.items())
print(game.keys())

item = []
mercado = []
for i in range(3):
    item.append(input('Digite o nome dp item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()
print(mercado)


merc = []
for i in range(3):
    prod = input('Digite o produto: ')
    qtd = int(input('Digite a qunatidade: '))
    valor = float(input('Digite o valor'))
    merc.append([prod,qtd,valor])
print(merc)


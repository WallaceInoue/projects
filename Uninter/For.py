for tab in range (1,11):
    print('tabuada do {}'.format(tab))
    for x in range (1,11):
        print('{} x {} = {}'.format(tab, x, tab*x))



tab = 1
while (tab <= 10):
    print('tabuada do {}'.format(tab))
    i = 1
    while (i <= 10):
        print('{} x {} = {}'.format(tab, i, tab*i))
        i+= 1
    tab += 1


soma = 0
qtd = 0
for x in range (1,7):
    if (x % 2 == 0):
        soma += x
        qtd += 1
media = soma/qtd
print('resultado {} numeros pares e a media é {}'.format(qtd,media))
print(soma)


for x in range (2,20,2):
    print(x)

for i in range (5):
    print(i)
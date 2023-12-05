print('digite uma frase para ser repitida')
print('digite "sair" para encerrar ')
while True:
    text = input('')
    print(text)
    if text == 'sair':
     break
print('encerrado')

x = int(input('Digite um numero'))
while (x <= 0):
    x = int(input('Digite um valor maior que zero: '))
print('Voce digitou o numero {}'.format(x))

n = 1
par = impar = 0
while (n != 0 ):
    n = int(input('digite um numero'))
    if n != 0:
     if ( n % 2 == 0):
        par = par + 1 # par += 1
     else:
        impar += 1
print('VOce digitou {} pars e {} impar.'.format(par, impar))


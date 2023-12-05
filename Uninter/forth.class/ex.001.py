n1 = int(input('Digite um valor para multiplicar'))
n2 = int(input('Digite outro valor para multiplicar por quantos'))
contador = 1
acumulador = 0
while (contador <= n2):

    print(acumulador)
    acumulador += n1
    contador += 1
print('{} x {} = {}'.format(n1,n2,acumulador))




# CONTINUE
while True:
    nome = input('Digite seu nome: ')
    if (nome != 'wallace'):
        continue
    senha = input('Qual sua senha: ')
    if (senha == 'inoue'):
        break
print('tudo ok!!!!')


# LOOP infinito com BREAK
print('Digite uma frase para ser exibida na tela \n'
      'Ou digite "sair" para encerrar')
while True:
    frase = input('>>')
    print(frase)
    if ( frase == 'sair'):
        break
print('encerrado!!!')


# VALIDANDO VALOR
x = int(input('Digite um numero maior que zero: '))
while(x < 1):
    x = int(input('Digite um numero maior que zero: '))
print('Você digitou {}'.format(x))


# ACUMULADOR
soma = 1
acumulador = 0
while(soma <= 5):
    nota = float(input('Qual sua {}° nota: '.format(soma)))
    soma += 1
    acumulador += nota
media = acumulador / soma
print('Sua media de nota é {}'.format(media))


# INCREMENTO
inicial = int(input('Digite numero inicial: '))
final = int(input('Digite numero final: '))
contador = inicial
while (contador <= final):
    if (contador % 2 == 0):
        print(contador)
    contador += 1
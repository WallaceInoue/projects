ano = int(input('Quantos anos você esta empresa?'))
salario = float(input('Qual seu ganho mensal?'))

if (ano < 5):
    bonus = salario * (10 / 100) # salario * 0.10
    print('Seu bonus será de R${}'.format(bonus))
else:
    bonus = salario * (20 / 100)
    print('Seu bonus será de R${}'.format(bonus))




nasc = int(input('Qual seu ano de nascimento?'))
ano = int(input('Ano atual: '))
ano -= nasc
print('Você tem {} anos'.format(ano))
#print('Você tem {} anos'.format(ano-nasc))

# Condição COMPOSTA
numero = int(input('Digite um numero para saber se é par ou impar: '))

if (numero % 2 == 0):
    print('O numero digitado "{}" é PAR'.format(numero))
else:
    print('O numero digitado "{}" é IMPAR'.format(numero))


# Condição SIMPLES
n1 = int(input('Digite um numero: '))
n2 = int (input('Digite o segundo numero: '))

if (n1 > n2):
    print('O primeiro numero digitado "{}" é maior que o segundo'.format(n1))




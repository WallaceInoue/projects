def valid(n):
    n = int(input('Digite um numero para calcular o fatorial(): '))
    while (n < 0):
        n = int(input('Digite um numero para calcular o fatorial(): '))
    return n


def fatorial(n1):
    if valid(n1):
        if (n1 == 0 or n1 == 1):
            return 1
        else:
            fat = 1
            for i in range(1, n1 + 1):

                fat *= i
            return fat
    else:
        return 'ERRO'


num = int(input('Digite um numero para calcular o fatorial: '))
res = fatorial(num)
print('o fatorla de {} é {}'.format(num, res))

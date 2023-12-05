a = int(input('LADO  A: '))
b = int(input('LADO  B: '))
c = int(input('LADO  C: '))

if(a > 0 and b > 0 and c > 0):
    if (a + b > c and b + c > a and a + c > b):
        if (a == b and b == c):
            print('triangulo equilatero')
        elif (a != b and b != c):
            print('triangulo tres lado diferente')
        else:
            print('triangulo dois lado diferente')

    else:
        print('Nao possivel forma uma triangulo')
else:
     print('Nao possivel forma uma triangulo')
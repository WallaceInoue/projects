print('------CALCULADORA------ \n'
      'Qual operaçâo deseja realizar \n'
      '+ = adiçâo\n'
      '- = subtraçâo\n'
      '* = multiplicaçåo\n'
      '/ = divisâo')
op = input('Operaçâo desejada: ')
if (op == '+' or op == '-' or op == '*' or op == '/'):


        n1 = float(input('primerio numero: '))
        n2 = float(input('segundo numero: '))

        if (op == '+'):
            print('{} + {} = {}'.format(n1,n2,n1+n2))
        elif(op == '-'):
            print('{} + {} = {}'.format(n1, n2,n1 - n2))
        elif( op == '*'):
            print('{} + {} = {}'.format(n1,n2,n1*n2))
        elif(op == '/'):
            print('{} + {} = {}'.format(n1, n2,n1 / n2))

else:
    print('Operaçâo invalida!!!!')

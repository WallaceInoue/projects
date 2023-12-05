def int_valid(perg,min,max):
    x = int(input(perg))
    while(x < min or x > max):
        x = int(input(perg))
    return x


def fatorial(num):
    fat = 1
    if (num ==0):
        return  fat
    for i in range(1,num+1):
        fat *= i
    return fat
x= int_valid('Digite um numero para calcular um fatorial: ',0,99999)
print('{}! = {} '.format(x,fatorial(x)))


def soma(x=0, y=0, z=0):
    """
    Function that
    :param x: value optiocinal
    :param y: value opticional
    :param z:
    :return:
    """

    return x+y+z

print(soma(2,5))
help(soma)
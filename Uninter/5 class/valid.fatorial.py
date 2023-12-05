def valid(per,min):
    x = int(input(per))
    while(x < min):
        x = int(input(per))
    return x
def fatorial(num):
    fat = 1
    if (num == 0 ):
        return fat
    for i in range(1,num+1):
        fat *= i
    return fat

#======= PROGRAMA PRINCIPAL ----------

n1 = valid('numero para fatorial: ', 0)
print('{}! = {}'.format(n1,fatorial(n1)))

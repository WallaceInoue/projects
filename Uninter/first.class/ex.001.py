# 3° EXERCICIO
f1 = input('Digite uma frase: ')
tam =  len(f1)
sf = f1 [:(tam//2)]
print(f1[-2:])
print(sf)

medade1 = f1[:len(f1)//2]
ultimo = f1[-2:]
print(ultimo)
print(medade1)

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1 + ' ' + s2 + ' ' + s3)
print(10 * (s1 + ' '))
print(s1 + ' ' + 2 * (s2 + ' ') + 3 * (s3 + ' '))
print(7 * (s1 + ' ' + s2 + ' '))
print(5 * (2*(s2)+s3 + ' '))

# 2° EXERCICIO = ALUGUEL DE CARRO


# o minimo valor
n1 = 10,20,30
print(max(n1))
print(min(n1))


soma = 1 + 2 + 3 + 4 + 5
media = (23+19+31) / 2
div = 403//73
sobra = 403%73
print('soma: {} \n'
      'media: {} \n'
      'divisao: {} \n'
      'sobra: {}\n'.format(soma , media , div , sobra) )
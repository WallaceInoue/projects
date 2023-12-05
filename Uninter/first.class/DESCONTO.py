# 1° EXERCICIO = DESCONTO
valor = float(input('Digite o valor do produto:'))
desconto = int(input('Qual o valor do desconto: '))
desc = valor * (desconto / 100)
total = valor - desc
print('O preço do produto é R${:.2f} \n'
      'O valor do desconto é de : {} \n'
      'VALOR FINAL : R${:.2f}'.format(valor,desc,total))
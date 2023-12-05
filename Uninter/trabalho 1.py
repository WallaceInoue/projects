print('Bem-vindos ao atacado Wallace Bueno Inoue')

# variaveis que irá receber os valores do usuario
valor = float(input('Digite o valor unitário do produto: '))
qtd = int(input('Digite a quantidade do produto desejável: '))
desc = 0

# Condições segundo o enunciado
if(qtd < 200):
    desc = 0
elif(qtd >= 200 and qtd < 1000):
    desc = 5
elif(qtd >= 1000 and qtd < 2000):
    desc = 10
else:
    desc = 15
# Calculo do valor total
valor_sem = valor * qtd
# Calculo do valor do desconto
valor_com = valor_sem - (valor_sem * desc / 100)

print('O valor total SEM desconto é de R$ {:.2f}'.format(valor_sem))
print('O valor total COM desconto de {}% é de R$ {:.2f}'.format(desc,valor_com))






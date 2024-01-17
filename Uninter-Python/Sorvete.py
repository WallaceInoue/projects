print('Bem-vindo a sorveteria do Wallace Bueno Inoue')
print('+-----------------------------------Cardápio--------------------------------------+')
print('| N° DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|    1        |        R$ 6,00         |       R$ 7,00      |      R$ 8.00        |')
print('|    2        |        R$ 11,00        |       R$ 13,00     |      R$ 15.00       |')
print('|    3        |        R$ 15,00        |       R$ 18,00     |      R$ 21.00       |')
print('+---------------------------------------------------------------------------------+')

soma = 0 # IMPORTANTE para somar os valor

while True:
# -------------------pergunta ao cliente ----------------------
    sabor = input('Entre com sabor desejado (tr/pr/es): ')

    if (sabor != 'tr' and sabor != 'pr' and sabor != 'es'):
        print()
        print('"Sabor de Sorvete Inválido"')
        continue

    bola = int(input('Entre com numero de bolas desejado (1 a 3): '))

    if (bola < 1 or bola > 3):
        print()
        print('"Quantidade de Bolas de Sorvetes Inválida"')
        continue

# ------------------------ MEnu ---------------------------------
    if (sabor == 'tr' and bola == 1):
        soma += 6
        print('Pedido de 1 bola de sorvete no sabor TRADICIONAL: R$ 6,00')

    elif(sabor == 'tr' and bola == 2):
        soma += 11
        print('Pedido de 2 bolas de sorvete no sabor TRADICIONAL: R$ 11,00')

    elif(sabor == 'tr' and bola == 3):
        soma += 15
        print('Pedido de 3 bolas de sorvete no sabor TRADICIONAL: R$ 15,00')

    elif(sabor == 'pr' and bola == 1):
        soma += 7
        print('Pedido de 1 bola de sorvete no sabor PREMIUM: R$ 7,00')
    elif(sabor == 'pr' and bola == 2):
        soma += 13
        print('Pedido de 2 bola de sorvete no sabor PREMIUM: R$ 13,00')
    elif(sabor == 'pr' and bola == 3):
        soma += 18
        print('Pedido de 3 bola de sorvete no sabor PREMIUM: R$ 18,00')

    elif(sabor == 'es' and bola == 1):
        soma += 8
        print('Pedido de 1 bola de sorvete no sabor ESPECIAL: R$ 8,00')
    elif(sabor == 'es' and bola == 2):
        soma += 15
        print('Pedido de 2 bola de sorvete no sabor ESPECIAL: R$ 15,00')
    elif(sabor == 'es' and bola == 3):
        soma += 21
        print('Pedido de 3 bola de sorvete no sabor ESPECIAL: R$ 21,00')

# ------------------------ Opção de continuar junto com o print do valor total ---------------------------------

    mais_pedido = input('deseja pedir mais? ("S" para continuar ou "N" para encerrar)')
    if(mais_pedido.lower() == 's'):
        print()
        continue # importante para voltar ao inicio de menu
    elif(mais_pedido.lower()== 'n'):
        print()
        print('Obrigado por comprar na sorveteria Wallace Bueno Inoue\n'
              'Valor total a ser pago: R$ {:.2f}'.format(soma))
        print()
        break # importante para quebrar o loop e mostra o total de soma


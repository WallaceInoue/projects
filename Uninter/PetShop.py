def cachorro_peso(msg): # Irá returnar o peso para o main
    while True: # Enquanto não digitar um valor numerico não sairá do loop
        try:
            peso = float(input(msg))
        except (ValueError, TypeError):# Tratara caso não for um valor numerico e retorna a pergunta
            print('ERRO')
            print('Digite apenas valores numericos!!')
            continue
        if(peso < 3):
            return 40
        elif(peso < 10):
            return 50
        elif(peso < 30):
            return 60
        elif(peso < 50):
            return 70
        else:
            print('Peso maximo permitido de até 50 Kg')
             #caso o usuario digite um valor maior que 50

def cachorro_pelo(msg): # Retornará o mutiplicador
    while True:
        pelo = str(input(msg)).strip().lower()
        if(pelo == 'c'):
            return 1
        elif(pelo == 'm'):
            return 1.5
        elif(pelo == 'l'):
            return 2
        else: # uma string diferente informado irá executar o else e voltar a pergunta
            print(f'A letra "{pelo}" invalida!!!')
            print('Válido apenas as letras anunciadas (c, m, l\n'
                  '')

def cachorro_extra(msg):
    acumulador = 0 # Soma as opções selecionadas e retorna o valor as digidar "0"
    while True:
        try:
            extra = int(input(msg))

            if(extra == 1):
                acumulador += 10
            elif(extra == 2):
                acumulador += 12
            elif(extra == 3):
                acumulador += 15
            elif(extra == 0):
                return acumulador
            else:
                print('Número inválido!!! Tente (0, 1, 2, 3)')
        except ValueError:
            print('Por favor, digite um valor numérico')


#----- Programa Principal -------
print('Bem-vindo ao petshop Wallace Bueno Inoue')
# as variaveis abaixo invoca as funçoes criadas a acima e os parâmetros de dentro são transferidos
peso = cachorro_peso('Qual o peso do cachorro (Kg)? ')
pelo = cachorro_pelo('Informe o tipo tamanho do pelo do cachorro: \n'
                     '>> Para cães com pelo curto = c \n'
                     '>> Para cães com pelo média = m \n'
                     '>> para cães com pelo longo = l\n'
                     '>>')
extra = cachorro_extra('Deseja adicionar algum serviço adicional?\n'
                       '0 = não desejo mais nada \n'
                       '1 = cortar unhas \n'
                       '2 = escovar os dentes \n'
                       '3 = limpar as orelhas \n'
                       '>>')
total = peso * pelo + extra

print(f'Total a pagar: R$ {total:.2f} (adicional(is): R$ {extra:.2f} + peso: {peso} * pelo:{pelo})')
cadastro = {'nome':[],'sexo':[],'ano':[]}

while True:
    fim = input('Deseja cadastrar uma pessoa? [NAO ou SIM]: ')
    if fim.upper() in 'NAO':
        break
    if fim.upper() not in 'SIM':
        print('Digite SIM ou NAO')

    nome = input('Qual seu nome?: ')
    sexo = input('Qual seu sexo?: ')
    ano = int(input('Qual seu ano de nascimento?: '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)

print(cadastro)
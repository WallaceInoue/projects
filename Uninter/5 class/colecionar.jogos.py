def valid(perg,min,max):
    x = int(input(perg))
    while(x < min or x > max):
        x = int(input(perg))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação')
    else:
        print('Arquivo criado')

def existe_arquivos(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarjogo(nomeArquivo, njogo, ngame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{}; {}\n'.format(njogo,ngame))
    finally:
        a.close()

def listararquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()

#------------- Main -------------------

arquivo = 'games.txt'

if existe_arquivos(arquivo):
    print('Arquivo localizado no PC')
else:
    print('Arquivo nao existe!!!')
    criaArquivo(arquivo)

while True:
    print('OPCÕES DE CADASTRO')
    print('1 = Cadastrar')
    print('2 = Listar cadastro')
    print('3 = Sair')

    op = valid('Escola opção desejada: ', 1, 3)
    if (op == 1):
        print('Cadastrar selecionado')
        njogo = input('Nome do jogo: ')
        ngame = input('Nome do game: ')
        cadastrarjogo(arquivo, njogo, ngame)

    elif(op == 2):
        print('Listar selecionado')
        listararquivo(arquivo)

    elif(op == 3):
        break
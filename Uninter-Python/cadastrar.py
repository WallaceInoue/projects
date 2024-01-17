from time import sleep
#---------------- Funções ------------------
def cadastrar_colaborador(id):
      print('Opção Cadastrar selecionado. \n'
            '')
      print(f'id do colaborador: {id}')
      nome = input('Entre com nome: ')
      setor =input('Entre com setor: ')
      pagamento = float(input('Entre com pagamento (R$): '))
      dictionary = {'id':id,
                     'nome':nome,
                     'setor':setor,
                     'pagamento':pagamento}
      lista_colaboradores.append(dictionary.copy())# a variável "dictionary" enviará uma copia para variável "lista_colaboradores"


def consultar_colaborador():
      print('Opção Consultar selecionado.')
      consultar = input('Você deseja:\n'
                        '1-Consultar TODOS\n'
                        '2-Consultar por ID\n'
                        '3-Consultar por SETOR\n'
                        '4-Retornar ao MENU\n'
                        '>>')
      if(consultar == '1'):
            print('Consultar todos...')
            sleep(1)
            for t in lista_colaboradores:
                  print('--------------------------------')
                  for k, v in t.items():
                        if(k == 'pagamento'): #essa contição faz apenas o print de "pagamento" para adicionar o R$
                              print(f'{k}: R$ {v:.2f}')
                        else:
                              print(f'{k}: {v}')

      elif(consultar == '2'):
            print('Consultar por id...')
            id = int(input('Entre com a id que deseja consultar: '))
            for i in lista_colaboradores:
                  if(i['id'] == id):
                        for k, v in i.items():
                              if (k == 'pagamento'):

                                    print(f'{k}: R$ {v:.2f}')
                              else:

                                    print(f'{k}: {v}')

      elif(consultar == '3'):
            print('Consultar por setor...')
            setor = input('Entre com setor deseja consultar: ')
            for s in lista_colaboradores:
                  if(s['setor'] == setor):
                        for k, v in s.items():
                              if (k == 'pagamento'):

                                    print(f'{k}: R$ {v:.2f}')
                              else:

                                    print(f'{k}: {v}')
      elif(consultar == '4'):
            return
      else:
            print('[ERRO]\n'
                  'Opção Inválida. Tente um número entre de 1 a 4.')


def remover_colaborador():
      print('Opção Remover selecionado.')
      while True:# Loop encerrará apenas quando o usuario entrar com a id correta caso contrario perguntará novamento
            remover = int(input('Entre com id que deseja remover: '))
            found = False # found recebe false e mudará se na interação com a lista
            for r in lista_colaboradores:
                  if(r['id'] == remover):
                        lista_colaboradores.remove(r)
                        print('Removido com sucesso!!')
                        found = True
                        return

            if not found: # caso nao haja uma interação permanecerá false
                  print('ID não encontrado.')
                  continue

#---------------- Main ---------------------
lista_colaboradores = [] # Lista receberá o dicionário pela função  cadastrar_colaborador(id)
id_global = 0
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print('| Bem-vindo ao Controle de Colaboradores do Wallace Bueno Inoue |')
print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

while True: # Um loop que apenas encerrará quando o usúario desejar
      print('')
      print('----------- MENU PRINCIPAL ----------- ')
      opcao = input('Escolha opção desejada:\n'
            '1-Cadastrar Colaborador\n'
            '2-Consultar Colaborador\n'
            '3-Remover Colaborador\n'
            '4-Encerrar Programa\n'
            '>>')
      if(opcao == '1'):
            id_global += 1 # contador para cada vez que selecionar opção 1 irá adicionar mais 1
            cadastrar_colaborador(id_global) # Invocará a função criada para cadastrar
      elif(opcao == '2'):
            consultar_colaborador()

      elif(opcao == '3'):
            remover_colaborador()

      elif(opcao == '4'):
            print('Programa Encerrado !!')
            break
      else: # Qualquer outro valor digitado além de 1 a 4 aparecerá um mensagem para corrigir
            print('[ERRO]\n'
                  'Opção Inválida. Tente um número entre de 1 a 4.')

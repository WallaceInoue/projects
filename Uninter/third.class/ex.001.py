cima = True
baixo = True
if ( cima  and baixo):
    print('decida!!!')
else:
    print('Voce esolheu um caminho')

ano = int(input('Seu ano: '))
if (ano % 4 == 0):
    print('Ano bissexto')
else:
    print('Nâo é um ano bissexto')



caminho = input('Qual caminho você escolhe (norte, sul, leste, oeste): ')
if (caminho == 'norte' or caminho == 'sul' or caminho == 'leste' or caminho == 'oeste'):
     print('Você escapou!!!')

dano = int(input('dano de ataque:'))
escudo = int(input('escudo'))
if (dano > 10 and escudo == 0):
    print('Você esta morto')


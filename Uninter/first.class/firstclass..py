# entrada
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade:'))
tam = len(nome)
ano = 2023-idade
print('fatiando nome {} \n'
      'e contando nome {}\n'
      'sua idade é {}\n'
      'então seu ano é {}'.format(nome[:2], tam, idade, ano))


# Tamanho de uma String
frase = 'Como saber tamanho de um string'
tamanho = len(frase)
print('Faça uma val com (len) antes e add a val que deseja contar entao o tamanho de FRASE é {}'.format(tamanho))

# Fatiar
s1 = 'Logica e algoritimos'
print(s1[0:6])

# Composiçãnota
nota = 8.5
print('Sua nota %.2f'%nota)


# Contetanação
s1 = 'A' + '-'*10+ 'B'
print(s1)

# o texto dentro de parenteses é a saida e depois da virgula é a operação aritimeticos
print('O resultado de 2+3=',2+3)

# Acessando o INDICE.
frase = ('Ola, mundo!!!')
print('O indice 2 de frase é: {}'.format(frase[2]))

numero =  10*5
print('O numero que irá aparecer da variavel numero é {} e quero acessar o indece da variavel 6 de frase {}'.format(numero,frase.upper()[6]))
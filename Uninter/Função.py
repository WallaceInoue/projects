def valid_string(perg,min,max):

    p1 = input(perg)
    tam = len(p1)
    while(tam < min or tam > max):
        p1 = input(perg)
        tam = len(p1)
    return p1



x = valid_string('Digite uma string (entre 5, 15 caracteres): ', 5, 15)
print('Você digitou {}. \n Dados válido .\n Encerramento do programa'.format(x))



def boi():
    ovos = 'Variavel Local boi'
    print(ovos)
def bacon():
    ovos = 'Variavel Local bacon'
    print(ovos)
    boi()
    print(ovos)
ovos = 'Variavel Global'
bacon()
print(ovos)



def borda(n1):
    tam = len(n1)
    if tam:
        print('+','-'*tam,'+')
        print('|',n1,'|')
        print('+','-'*tam,'+')
borda('Ola, Mundo')
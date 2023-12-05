# Cria Função
def borda(frase):
    tam = len(frase)
    if tam:
        print('+','-'*tam,'+')
        print('|',frase,'|')
        print('+','-'*tam,'+')
# programa principal que vai chamar a funçao
borda('wallace')


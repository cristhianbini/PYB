def parabens():
    print(' Parabéns pra você\n Nessa data querida\n Muitos anos de vida\n')
    
parabens()

def temLetrau():
    frase = input('Digite uma frase:')
    if 'u' in frase:
        print('Você usou a letra U')
    else:
        print('Você não usou a letra U')
        
temLetrau()

def somaQuadrados(a,b):
    somaQ = a**2 + b**2
    return somaQ

somaQuadrados(2,3)

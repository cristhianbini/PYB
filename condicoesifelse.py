#Condições if, else, elif
#if significa se isso não for verdade ou se for verdade
#else significa que se não for então responda isso

#se isso é verdade então faça isso:

tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')

#Outra forma de fazer mais simplificada

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo<=3 else 'carro velho')
print('--FIM--')

#Exemplo de programa com essas condições

nome = str(input('Qual seu nome? '))
if nome == 'Cristhian':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

#Preço médio notas escola

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
      



    


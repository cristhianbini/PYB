#Formulário

nome = input('Escreva seu nome:')
mae = input('Escreva nome da sua mãe:')
pai = input('Escreva nome do seu pai:')
filho = input('Escreva nome do seu filho:')

with open('cadastro.txt', 'w') as cadastro:
    print(nome,mae,pai,filho, file=cadastro)

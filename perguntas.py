#Perguntas

nome = input ('Qual seu nome? ')
print('Muito prazer em conhecê-lo,', nome)

idade = input ('Qual sua idade? ')
print('Uma idade ótima,', idade, 'anos é novo ainda!')

peso = input ('Qual seu peso? ')
print('Só isso,',peso, 'é ideal pra você!')

namora = input ('Esta estudando? ')
print('Já sei programação Python!')

trabalho = input ('Tem estudado muito? ')
print('Estudar muito é preciso.')

prazer = input ('Gosta do que faz? ')
print('Também adoro ser robô rs...')

print('Posso te ajudar em algo mais?')

perguntar = input ()

with open('respostas.txt', 'w') as respostas:
    print(nome,idade,peso,namora,trabalho,prazer,perguntar, file=respostas)

    

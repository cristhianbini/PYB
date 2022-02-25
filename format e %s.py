#Entre aspas sempre é uma str então uso %s.

fruta = 'cupuaçu'
type (fruta)
print ('Suco de cupuaçu é meu favorito!')
print('Suco de %s é meu favorito!' %fruta)

#Variavel sem aspas e numero fica %d de decimal

ano = 1980
type(fruta)
print('Eu nasci no ano', ano)
print('Eu nasci no ano %d!' %ano)
print(ano)

#Variavel pode ser do tipo float que são numeros seguidos de virgulas.

juros = 10.5
type(juros)
print('Quero receber esses juros mensais')
print('Quero receber esses juros %f mensais! ' %juros)
print(juros)

#Variaveis podem ser informadas no meio do código com chaves{} seguido de .format mais variavel ao final dos parentes. 

print('Suco de {} é o meu favorito!'.format(fruta))

#Variavel com o uso do .format

cor0 = 'azul'
cor1 = 'verde'
cor2 = 'rosa'
print('O céu é {0}, a flor é {1} e meu carro é {2}'.format(cor0,cor1,cor2))

#Variavel com o float que não imprime todos os numeros depois da virgula.

conta = 17/3
print(conta)
print('O resultado da conta é:{}'.format(conta))
print('O resultado da conta é:{:.2f}'.format(conta))







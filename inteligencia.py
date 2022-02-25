#Inteligencia

perguntar = input ('Posso te ajudar a responder alguma duvida? ')
print('Isso te ajudou?')

with open('inteligencia.txt', 'w') as inteligencia:
    print(perguntar, file=inteligencia)

    

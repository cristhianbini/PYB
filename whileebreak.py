import time
contador = 0
while contador < 10:
    print('Ainda não deu certo!')
    contador = contador + 1
    if contador == 6:
        break
    time.sleep(1)
print('Agora deu certo!')

#Fatorial de 4! = 4*3*2*1

numero = int(input('Digite um numero qualquer: '))
fatorial = numero
contador = 1
#fatorial = numero*(numero-1)*(numero-2)*(numero-3)
while (numero-contador)>1:
    fatorial = fatorial*(numero-contador)
    contador += 1
    time.sleep(1)
print('{}! = {}'.format(numero,fatorial))






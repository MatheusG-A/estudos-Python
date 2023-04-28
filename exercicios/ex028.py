from random import randint
from time import sleep
computador = randint(0, 5)
print('--------------------------------------')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens!, Você conseguiu me vencer"')
else:
    print('Ganhei! Eu pensei no númeor {} e não no {}!'.format(computador, jogador))
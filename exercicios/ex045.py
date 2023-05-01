from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp= randint(0,2)
a = int(input('''=-=-=-=-=-=-=-=-=-
ESCOLHA! Jo KEn Pô
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
: '''))
print("JO")
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('-=-'*12)
print('Computador jogu {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[a]))
print('-=-'*14)
if comp == 0:
    if a == 0:
        print('EMPATE!')
    elif a == 1:
        print('VOCÊ GANHOU!')
    elif a ==2:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVALIDA')
elif comp == 1:
    if a == 0:
        print('VOCÊ PERDEU')
    elif a == 1:
        print('EMPATE!')
    elif a ==2 :
        print('VOCÊ GANHOU!')
    else:
        print('JOGADA INVALIDA!')
elif comp ==2:
    if a == 0:
        print('VOCÊ GANHOU!')
    elif a == 1:
        print('VOCÊ PERDEU!')
    elif a == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA.')
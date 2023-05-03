print('''===================
10 TERMOS DE UMA PA
=======================''')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decima = termo + (10) * razao
for c in range(termo, decima, razao):  
    print('{}'.format(c), end='- ')
print('ACABOU')
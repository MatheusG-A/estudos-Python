
dis = float(input('Qual é a distancia da sua viagem? '))
if dis <= 200:
    preço = dis * 0.5
else:
    preço = dis * 0.45
print('O preço da sua passagem será de \033[1;32mR${:.2f}\033[m'.format(preço))

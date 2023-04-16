n1=float(input('Qual é o salario do funcionario? R$'))
n2= n1 + (n1*15/100)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}.'.format(n1,n2))
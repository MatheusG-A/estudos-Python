valor = float(input('Valor da casa: R$\033[32m'))
salario = float(input('\033[mSalario do comprador: R$\033[32m'))
ano = int(input('\033[mQuantos anos de financiamento? \033[32m'))
parcelas = valor / (ano * 12)
print('\033[mPara pagar um casa de R${} em {} anos a prestação será de R${:.2f}'.format(valor, ano, parcelas))
if parcelas <= salario*30/100:
    print('Empréstimo pode ser CONCEDIDO !')
else:
    print('Espréstimo\033[31m NEGADO !\033[m')
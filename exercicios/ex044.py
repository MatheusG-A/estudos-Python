valor = float(input('Qual o preço da compra? R$\033[32m'))
print('\033[m=-='*13)
print('''Qual vai ser a forma de pagamento?
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] PARCELADO ATÉ 2X NO CARTÃO
[ 4 ] PARCELADO EM 3X OU MAIS NO CARTÃO''')
print('=-=' *14)
op = int(input('    ESCOLHA UMA OPÇÃO: '))
if op == 1:
    total = valor - (valor * 10/100)
    print('Sua compra teve com desconte de 10%!')
elif op == 2:
    total = valor - (valor * 5/100)
    parcela = valor / 2
    print('Sua compra tera um desconto de 5%!')
elif op == 3:
    print('Sua compra sera parceladas em 2X se R${:.2f}')
elif op == 4:
    total = valor + (valor * 20/100)
    totaparc = int(input('Quantas parcelas? '))
    parcela = total / totaparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totaparc,parcela))
else:
    total = valor
    print('\033[31mOPÇÃO INVALIDA TENTE NOVAMENTE.\033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
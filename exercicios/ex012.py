n1=float(input('Digite o preço do produto: R$'))
n2= n1 - (n1*5/100)


print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(n1, n2))
s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        s = s + num
        cont += 1
print(' Você informou {} números PARES e a soma foi {}'.format(cont, s))
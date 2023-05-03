f = str(input('Digite um frase: ')).strip().upper()
p = f.split()
junto = ''.join(p)
inver = ''
for letra in range(len(junto) - 1, -1, -1):
    inver += junto[letra]
print('O inverso de {} é {}'.format(junto, inver))
if inver == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')


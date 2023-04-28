print('=-='*12)
print('ANALISANDO TRINGULOS')
print('-=-'*12)
n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))
if n1 < n2 + n3 and n3 < n1 + n2 and n2 < n3 + n1:
    print('È posivel formar um triangulo!')
else:
    print('Esse seguimentos NÃO formam um triangulo!')
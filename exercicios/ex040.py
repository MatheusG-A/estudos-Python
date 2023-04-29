n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está aprovado.')
elif 7 > m >= 5 :
    print('O aluna está de RECUPERAÇÃO>')
else:
    print('Aluno REPROVADO.')

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
if idade == 18:
    print('Você tem que se alistar esse ano')
elif idade < 18:
    saldo = 18 - idade
    print(' Ainda falta {} anos para o alistamento'.format(saldo))
    ano1 = atual - saldo
    print('ainda falta {} anos para seu alistamento.'.format(ano1))
elif idade > 19:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano1 = atual - saldo
    print('Seu alistamento foi em {}'.format(ano1))
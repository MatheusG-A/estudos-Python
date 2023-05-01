from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('Com {} anos é categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Com {} anos é categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Com {} anos é categoria JUNIOR'.format(idade))
elif idade <=25:
    print('Com {} anos é categoria SÊNIOR'.format(idade))
else:
    print('Com {} anos é categoria MASTER'.format(idade))
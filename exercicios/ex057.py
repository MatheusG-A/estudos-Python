sexo = str(input('Informe seu SEXO: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Porfavor, informe seu sexo: '))
print('Sexo {} registrado com sucesso.'.format(sexo))

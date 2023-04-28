salario = float(input(' Qual é o salário do funcionario? R$'))
if salario >= 1250:
    n = salario + salario * 10 / 100
else:
    n = salario + salario * 15 / 100

print('O novo Salario do funcionario é \033[1;32mR${:.2f}\033[m]'.format(n))

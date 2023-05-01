peso = float(input('Qaul é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)
print(' O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Está no peso IDEAL')
elif 25 <= imc < 30:
    print('Está com SOBREPESO')
elif 30 <= imc < 40:
    print('Está com OBESIDADE')
else:
    print('Está com OBESIDADE MÓRBIDA')
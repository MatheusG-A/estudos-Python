dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Qunatos km foram percorridos? '))
n1 = (60 * dias) + (km * 0.15)

print("Você tera que pagar pelo aluguel: R${:.2f} .".format(n1))
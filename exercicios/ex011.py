n1=float(input('Largura da parede: '))
n2=float(input('Altura da parede: '))
a=n1*n2
t= a/2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².\n Para pintar essa parede, você precisará de {}l de tinta.'.format(n1, n2,a, t))
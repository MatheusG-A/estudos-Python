import math
a = float(input('Digite o angulo que você desaja: '))
seno = math.sin(math.radians(a))
print('O ângulo de {}, tem o SENO de {:.2f}'.format(a, seno))
cosseno = math.cos(math.radians(a))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(a, cosseno))
tangente = math.tan(math.radians(a))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a, tangente))
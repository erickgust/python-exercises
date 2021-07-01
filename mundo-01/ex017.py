from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
print('O comprimento da Hipotenusa desse triângulo retângulo é {:.2f}.'.format(hypot(co, ca)))

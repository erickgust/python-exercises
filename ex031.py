d = float(input('Qual a distância da viagem? '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print('O preço da passagem foi de {:.2f}!'.format(p))
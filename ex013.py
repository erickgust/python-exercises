s = float(input('Qual é o salário do funcionário? R$'))
ns = s+(s*0.15)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(s, ns))

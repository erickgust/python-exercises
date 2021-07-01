v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    m = (v-80) * 7
    print('O VALOR DA MULTA É DE R${:.2f}!'.format(m))
else:
    print('Está dentro da velocidade permitida. Tenha um bom dia!')

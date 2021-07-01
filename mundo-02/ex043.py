peso = float(input('Digite seu peso (Kg): '))
alt = float(input('Digite sua altura (m): '))
imc = peso / alt ** 2
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif 40 <= imc:
    print('Obesidade mórbida')
print('O seu IMC é de {:.2f}.'.format(imc))

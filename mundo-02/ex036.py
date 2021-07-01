vcasa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos vai pagar? '))


if vcasa / (12 * anos) > sal * 0.3:  # Valor da prestação mensal
    print('NEGADO! O valor da prestação excede mais de 30% do seu salário mensal.')
elif vcasa / (12 * anos) <= sal * 0.3:
    print('APROVADO! Seu salário atende aos requisitos.')

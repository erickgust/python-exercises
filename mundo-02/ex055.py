menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Digite o peso (Kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O MAIOR peso foi {}Kg e o MENOR foi {}Kg'.format(maior, menor))

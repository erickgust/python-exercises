r = 'S'
quant = tot = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    if quant == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    quant += 1
    tot += n
m = tot / quant
print('Você digitou {} números e a média foi de {}'.format(quant, m))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

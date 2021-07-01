num = list()
numpar = list()
numimpar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ask == 'N':
        break
for c in num:
    if c % 2 == 0:
        numpar.append(c)
    else:
        numimpar.append(c)
print(f'A lista completa é {num}')
print(f'A lista de pares é {numpar}')
print(f'A lista de ímpares é {numimpar}')
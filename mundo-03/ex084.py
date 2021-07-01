pessoas = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados.copy())
    dados.clear()
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ask == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de', end=' ')
for peso in pessoas:
    if peso[1] == mai:
        print(f'[{peso[0]}]', end=' ')
print(f'\nO menor peso foi de {men}Kg. Peso de', end=' ')
for peso in pessoas:
    if peso[1] == men:
        print(f'[{peso[0]}]', end=' ')

num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    if num.count(num[-1]) >= 2:
        print('Valor duplicado! Não vou adicionar...')
        num.pop()
    else:
        print('Valor adicionado com sucesso...')
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ask == 'N':
        break
print('-='*30)
num.sort()
print(f'Você digitou os valores {num}')

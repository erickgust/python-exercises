num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ask == 'N':
        break
num.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(num)} elementos.')
print(f'Os valores em ordem descrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
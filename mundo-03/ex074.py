from random import randint
tabela = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in range(0, 5):
    if c == 0:
        maior = tabela[0]
        menor = tabela[0]
    else:
        if tabela[c] > maior:
            maior = tabela[c]
        if tabela[c] < menor:
            menor = tabela[c]
    print(tabela[c], end=' ')
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

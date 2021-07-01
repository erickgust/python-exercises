from random import randint
tabela = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in tabela:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi {max(tabela)}')
print(f'O menor valor sorteado foi {min(tabela)}')

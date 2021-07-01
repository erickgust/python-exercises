valores = list()
for contador in range(5):
    valores.append(int(input(f'Digite um valor para a Posição {contador}: ')))
print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for pos, maior in enumerate(valores):
    if maior == max(valores):
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for pos, menor in enumerate(valores):
    if menor == min(valores):
        print(f'{pos}...', end=' ')
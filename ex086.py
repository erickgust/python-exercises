matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for col in range(3):
    for lin in range(3):
        matriz[col][lin] = (int(input(f'Digite um valor para [{col}, {lin}]: ')))
print('-=' * 30)
for col in range(3):
    for lin in range(3):
        print(f'[{matriz[col][lin]:^5}]', end=' ')
    print()
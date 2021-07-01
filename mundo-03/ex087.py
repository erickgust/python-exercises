matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma3 = 0
for c in range(3):
    for l in range(3):
        matriz[c][l] = int(input(f'Digite um valor para [{c}, {l}]: '))
        if matriz[c][l] % 2 == 0:
            par += matriz[c][l]
        if matriz[2]:
            soma3 += matriz[c][2]
print('-=' * 30)

for c in range(3):
    for l in range(3):
        print(f'[{matriz[c][l]:^5}]', end=' ')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

num = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
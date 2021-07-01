print('='*31)
print(f'{" 10 TERMOS DE UMA PA ":^31}')
print('='*31)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
ultimo = a1 + (10 - 1) * r
for c in range(a1, ultimo + r, r):
    print('{} '.format(c), end='')
print('='*31)
print(f'{" 10 TERMOS DE UMA PA ":^31}')
print('='*31)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
print('PA (', end='')
while c <= 10:
    print('{}'.format(a1), end='')
    print(', ' if c < 10 else ')', end='')
    c += 1
    a1 += r

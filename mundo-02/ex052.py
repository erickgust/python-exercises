print('\033[1;36mCALCULADORA DE NÚMEROS PRIMOS\033[m')
print('\033[1;35m-=\033[m'*15)
n = int(input('\033[1mDigite um número inteiro: '))
s = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        s += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print()
print('\033[1;35m-=\033[m'*15)
if s == 2:
    print('\033[1;32mO número {} é PRIMO.'.format(n))
else:
    print('\033[1;31mO número {} NÃO é primo.'.format(n))
print('\033[1;35m-=\033[m'*15)

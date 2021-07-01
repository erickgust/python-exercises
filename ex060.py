print('-='*14)
print(f'{"Calculadora de Fatorial":^28}')
print('-='*14)
num = int(input('Digite um número inteiro: '))
c = num
f = 1
while c > 0:
    f *= c
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)
print('-='*14)
print('O fatorial de {} foi {}'.format(num, f))
print('='*31)
print(f'{" 10 TERMOS DE UMA PA ":^31}')
print('='*31)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a1
c = 0
while c < 10:
    print(termo, end=' → ')
    termo += r
    c += 1
print('PAUSA')
perg = False
n = 0
quantia = c
while not perg:
    n = int(input('Quantos termos você quer mostrar a mais? '))
    if n != 0:
        quantia += n
        while n > 0:
            print(termo, end=' → ')
            termo += r
            n -= 1
        print('PAUSA')
    else:
        perg = True
print('Progressão finalizada com {} termos mostrados.'.format(quantia))
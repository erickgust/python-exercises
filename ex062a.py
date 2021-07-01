print('='*31)
print(f'{" 10 TERMOS DE UMA PA ":^31}')
print('='*31)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(termo, end=' → ')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

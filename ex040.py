n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média foi de {:.1f}'.format(m))
if m < 5.0:
    print('\033[1;31mALUNO REPROVADO!')
elif 5.0 <= m < 7:
    print('\033[1;33mALUNO EM RECUPERAÇÃO!')
elif m >= 7:
    print('\033[1;32mALUNO APROVADO!')

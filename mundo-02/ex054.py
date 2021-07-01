from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Das 7 pessoas, {} são MAIORES de idade, '.format(maior), end='')
print('e {} são MENORES de idade.'.format(menor))

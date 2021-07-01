print('='*30)
print(f"{'BANCO CEV':^30}")
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
if valor >= 50:
    c = valor // 50
    valor %= 50
    print(f'Total de {c} cédulas de R$50')
if 20 <= valor < 50:
    c = valor // 20
    valor %= 20
    print(f'Total de {c} cédulas de R$20')
if 10 <= valor < 20:
    c = valor // 10
    valor %= 10
    print(f'Total de {c} cédulas de R$10')
if 0 < valor < 10:
    print(f'Total de {valor} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

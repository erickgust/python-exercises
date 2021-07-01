print('-'*30)
print(f"{'LOJA SUPER BARATÃO':^30}")
print('-'*30)
c = total = maior1000 = barato = 0
nomem = ''
while True:
    c += 1
    nome = str(input('Nome do Produto: ')).strip().title()
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        maior1000 += 1
    if c == 1 or preço < barato:
        barato = preço
        nomem = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f"{' FIM DO PROGRAMA ':-^40}")
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomem} que custa R${barato}')

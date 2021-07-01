preco = float(input('Qual o preço do produto? R$'))
print('''[1] À vista - dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros''')
resp = int(input('Qual a condição de pagamento? '))
if resp == 1:
    desc = preco - (preco*0.1)
    print('O valor do seu produto de R${:.2f} ficou por R${:.2f}, com 10% de desconto.'.format(preco, desc))
elif resp == 2:
    desc = preco - (preco*0.05)
    print('O valor do seu produto de R${:.2f} ficou por R${:.2f}, com 5% de desconto no cartão.'.format(preco, desc))
elif resp == 3:
    print('O valor do produto não se altera, sendo no total {:.2f} e em 2x por {:.2f}.'.format(preco, preco/2))
elif resp == 4:
    desc = preco + (preco*0.2)
    print('O valor do seu produto de R${:.2f} ficou por R${:.2f}, com 20% de juros no cartão.'.format(preco, desc))
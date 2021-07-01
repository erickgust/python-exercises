ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print('-' * 30)
        print(f'Você digitou o número {ext[n]}.')
        print('-' * 30)
    else:
        print('Tente novamente.', end=' ')
    ask = ' '
    while ask not in 'SsNn':
        ask = str(input('Quer continuar? [S/N] '))
    if ask in 'Nn':
        print('Finalizando...')
        break

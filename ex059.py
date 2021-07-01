from time import sleep
print('-='*10)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
r = 0
while r != 5:
    print('-='*10)
    print('''[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Novos números
[5] Sair do programa''')
    print('-=' * 10)
    r = int(input('Escolha: '))
    if r == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1+n2))
    elif r == 2:
        print('A multiplicação entre {} e {} resulta em: {}'.format(n1, n2, n1*n2))
    elif r == 3:
        if n1 > n2:
            print('O maior valor é {}.'.format(n1))
        elif n2 > n1:
            print('O maior valor é {}.'.format(n2))
        else:
            print('Não existe maior, ambos são iguais.')
    elif r == 4:
        n1 = int(input('Digite o novo valor: '))
        n2 = int(input('Digite outro novo valor: '))
    elif r == 5:
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(1.5)
print('-='*10)
print('Fim do programa!')
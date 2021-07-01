from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vezes = 0
while True:
    jog = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jog + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*30)
    print(f'Você jogou {jog} e o computador {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*30)
    if tipo == 'P' and total % 2 == 0 or tipo == 'I' and total % 2 == 1:
        vezes += 1
        print('Você VENCEU!')
    else:
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
    print('=-' * 15)
print('=-'*15)
print(f'GAME OVER! Você venceu {vezes} vezes.')

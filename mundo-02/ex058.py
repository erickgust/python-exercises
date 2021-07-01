from random import randint
print('Pensando... Um número entre 0 e 10...')
r = randint(0, 10)
p, s = 11, 0
while p != r:
    p = int(input('Em qual número eu pensei? '))
    print('-='*13)
    print('PROCESSANDO...')
    print('-=' * 13)
    s += 1
    if p == r:
        print('\033[32mPARABÉNS! Você acertou!\033[m')
        if s > 1:
            print('\033[33mMas você precisou de {} tentativas.\033[m'.format(s))
    else:
        print('\033[31mNão foi dessa vez! Tente novamente.\033[m')
print('-='*13)
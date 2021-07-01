from random import randint
from time import sleep
print('Pensando... Um número entre 0 e 5...')
r = randint(0, 5)
p = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if p == r:
    print('PARABÉNS! Você acertou!')
else:
    print('Não foi dessa vez! O número correto era {}!'.format(r))
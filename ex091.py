from random import randint
from time import sleep
from operator import itemgetter
pessoas = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in pessoas.items():
    print(f'    O {k} tirou {v}')
    sleep(1)
ranking = sorted(pessoas.items(), key=itemgetter(1), reverse=True)
print('-='*15)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f'    {i+1    }° lugar: {v[0]} com {v[1]}')
    sleep(1)

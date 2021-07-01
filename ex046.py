from emoji import emojize
from time import sleep
print(f'{" CONTAGEM REGRESSIVA ":=^30}')
for c in range(10, -1, -1):
    print('{}...'.format(c))
    sleep(1)
print(emojize(':party_popper: :party_popper: :party_popper:'))

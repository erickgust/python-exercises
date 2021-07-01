from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
somaPar(numeros)

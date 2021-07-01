from time import sleep


def maior(*parametros):
    print('-='*30)
    print('Analisando os valores passados...')
    mai = 0
    for c in parametros:
        if c > mai:
            mai = c
        print(c, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(parametros)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

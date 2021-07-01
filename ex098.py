from time import sleep


def contador(a, b, c):
    print('-='*20)
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(1.5)
    if a > b:
        for c in range(a, b-1, -c):
            print(c, end=' ')
            sleep(0.3)
    else:
        for c in range(a, b+1, c):
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, -2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input(f'{"Início:":<8}'))
fim = int(input(f'{"Fim:":<8}'))
salto = int(input(f'{"Passo:":<8}'))
contador(inicio, fim, salto)

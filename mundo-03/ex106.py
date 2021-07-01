from time import sleep
c = ('\033[m',     # 0 - sem cor
     '\033[41m',   # 1 - vermelho
     '\033[42m',   # 2 - verde
     '\033[43m',   # 3 - amarelo
     '\033[44m',   # 4 - azul
     '\033[45m'    # 5 - roxo
     '\033[7;30m'  # 6 - branco
     )


def ajuda(com):
    linhas(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def linhas(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')
    sleep(1)


linhas('SISTEMA DE AJUDA PyHELP', 2)
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
linhas('ATÉ LOGO', 1)
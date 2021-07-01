jogador = {}
equipe = []
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    print('-' * 35)
    for c in range(part):
        gols.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    print('-' * 35)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    equipe.append(jogador.copy())
    while True:
        ask = str(input('\033[1;33mQuer continuar? [S/N] \033[m')).strip().upper()[0]
        if ask in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if ask == 'N':
        break
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(equipe):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(equipe):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {equipe[busca]["nome"]}:')
        for i, g in enumerate(equipe[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

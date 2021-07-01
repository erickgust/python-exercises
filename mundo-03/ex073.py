from random import choice
tabela = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Palmeiras', 'Fluminense', 'Corinthians',
          'Santos', 'Ceará', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza', 'Bahia',
          'Goiás', 'Botafogo', 'Coritiba')
random = choice(tabela)
print(f'Lista de times do Brasileirão: {tabela}')
print(f'Os 5 primeiros são {tabela[:5]}')
print(f'Os 4 últimos são {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'O {random} está na {tabela.index(random)+1}ª posição')
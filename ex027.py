nome = input('Seu nome completo: ')
nomeS = nome.split()
print('Primeiro nome: {}'.format(nomeS[0]))
nomeRF = nome.strip().rfind(' ')
print('Último nome: {}'.format(nome[nomeRF+1:]))
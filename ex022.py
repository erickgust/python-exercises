nomec = str(input('Digite seu nome completo: ')).strip()
print('O nome com todas as letras maiúsculas: {} '.format(nomec.upper()))
print('O nome com todas as letras minúsculas: {} '.format(nomec.lower()))
nomeS = nomec.split()
print('Seu nome completo tem o total de: {} letras'.format(len(''.join(nomeS))))
print('O seu primeiro nome tem um total de: {} letras'.format(len(nomeS[0])))
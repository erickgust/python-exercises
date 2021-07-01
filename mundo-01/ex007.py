nome = input('Digite seu nome: ')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média do aluno {} foi {:.1f}'.format(nome, m))
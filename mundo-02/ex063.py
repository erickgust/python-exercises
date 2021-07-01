print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
c = 0
f1 = 0
f2 = 1
while c < termos:
    print(f1, end=' → ')
    f3 = f1 + f2
    f2 = f1
    f1 = f3
    c += 1
print('FIM')
print('~'*30)

'''while c < termos:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    c += 1'''
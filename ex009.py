t = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
c = 0
while c < 10:
    c = c + 1
    print('{} x {:2} = {}'.format(t, c, (t*c)))
print('-'*12)

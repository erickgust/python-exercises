t = int(input('Qual tabuada você deseja ver? '))
print('-'*12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(t, c, t*c))
print('-'*12)

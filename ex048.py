s = 0
tot = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        tot += 1
        s += c
print('A soma dos números foi de: {}'.format(s))
print('Foram {} números somados.'.format(tot))

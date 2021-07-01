n = t = s = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        s += n
        t += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(t, s))
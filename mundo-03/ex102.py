def fatorial(num=1, show=False):
    print('-' * 30)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            print('x ' if c > 1 else '= ', end='')
        f *= c
    return f


print(fatorial(5, True))

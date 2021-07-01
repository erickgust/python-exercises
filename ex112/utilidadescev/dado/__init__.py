def leiaDinheiro(msg):
    válido = False
    while not válido:
        n = str(input(msg)).strip().replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[31mERRO! \"{n}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(n)

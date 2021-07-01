def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
    return n


numero_int = leiaInt('Digite um Inteiro: ')
numero_real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numero_int} e o real foi {numero_real}')

while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if tabuada < 0:
        break
    for contador in range(1, 11):
        resultado = tabuada * contador
        print(f'{tabuada} x {contador:>2} = {resultado}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
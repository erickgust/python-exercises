def aumentar(preco=0, taxa=0, formato=False):
    valor = preco + (preco*(taxa/100))
    return valor if formato is False else moeda(valor)


def diminuir(preco=0, taxa=0, formato=False):
    valor = preco - (preco * (taxa / 100))
    return valor if formato is False else moeda(valor)


def dobro(preco=0, formato=False):
    valor = preco * 2
    return valor if formato is False else moeda(valor)


def metade(preco=0, formato=False):
    valor = preco / 2
    return valor if formato is False else moeda(valor)


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco, porcAu=10, porcRed=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{porcAu}% de aumento: \t{aumentar(preco, porcAu, True)}')
    print(f'{porcRed}% de redução: \t{diminuir(preco, porcRed, True)}')


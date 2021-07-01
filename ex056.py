velho = 0
s = 0
m = 0
nome1 = str
for c in range(1, 5):
    print(f'{" {}ª PESSOA ":-^22}'.format(c))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    m += idade
    if idade > velho and sexo in 'Mm':
        velho = idade
        nome1 = nome
    if idade < 20 and sexo in 'Ff':
        s += 1
print('A idade média do grupo é {} anos.'.format(m/4))
print('O nome do homem mais velho é {} com {} anos.'.format(nome1, velho))
print('Ao total tem {} mulheres com menos de 20 anos.'.format(s))

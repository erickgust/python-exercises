maior18 = homens = mulherid = 0
while True:
    print('-'*30)
    print(f"{'CADASTRE UMA PESSOA':^30}")
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 30)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherid += 1
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulherid} mulheres com menos de 20 anos')

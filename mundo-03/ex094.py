pessoa = {}
grupo = []
tot = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    tot += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        ask = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if ask in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if ask == 'N':
        break
media = tot / len(grupo)
print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram:', end=' ')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
print('\n<< ENCERRADO >>')

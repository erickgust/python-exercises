from datetime import date
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
if idade <= 9:
    print('Atleta MIRIM.')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')

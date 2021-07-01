from datetime import date
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
if idade < 18:
    print('Falta {} anos para você se alistar. \nSeu alistamento será em {}.'.format(18-idade, nasc+18))
elif idade == 18:
    print('Está na hora de se alistar. \nSe aliste agora.')
elif idade > 18:
    print('Já passou {} anos do seu alistamento. \nSeu alistamento foi em {}.'.format(idade-18, nasc+18))

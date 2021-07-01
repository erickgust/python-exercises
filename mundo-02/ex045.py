from random import choice
esc = str(input('Escolha entre pedra/papel/tesoura: ')).upper()
pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if pc == esc:
    print('EMPATE! Jogue novamente.')
elif (pc == 'PEDRA' and esc == 'PAPEL') or (pc == 'TESOURA' and esc == 'PEDRA') or (pc == 'PAPEL' and esc == 'TESOURA'):
    print('VOCÊ VENCEU! \nComputador jogou {}'.format(pc))
elif (esc == 'PAPEL' and pc == 'TESOURA') or (esc == 'PEDRA' and pc == 'PAPEL') or (esc == 'TESOURA' and pc == 'PEDRA'):
    print('VOCÊ PERDEU! \nComputador jogou {}'.format(pc))
else:
    print('ALTERNATIVA ERRADA')
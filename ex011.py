L = float(input('Qual é a largura da parede? '))
A = float(input('Qual a altura da parede? '))
Ar = L * A
T = Ar / 2
print('A área total da parede é de {}m². \nA quantia em litros de tinta usada é de: {:.1f}l.'.format(Ar, T))

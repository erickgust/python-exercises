frase = input('Digite o nome da cidade: ')
lista = frase.split()

if lista[0].title() == 'Santo':
    print('Essa cidade começa com "Santo"')
else:
    print('Essa cidade não começa com "Santo"')

print('Sua cidade começa com "Santo"? {}'.format('Santo' in lista[0].title()))


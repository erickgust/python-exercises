print('\033[1;34mÉ POLÍNDROMO OU NÃO É?\033[m')
print('\033[1;35m=\033[m'*22)
frase = str(input('\033[1mDigite uma frase: ')).upper()
lista = ''.join(frase.split())
print('\033[1;35m=\033[m'*22)
if lista == lista[::-1]:
    print('\033[1;32mEssa frase é um POLÍNDROMO')
else:
    print('\033[1;31mEssa frase NÃO é um POLÍNDROMO')

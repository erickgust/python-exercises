numero = int(input('Digite um número inteiro: '))
print('''Escolha para qual deseja converter:
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')
resposta = int(input('Digite: '))
if resposta == 1:
    print('O valor {} em Binário é: {}'.format(numero, bin(numero)[2:]))
elif resposta == 2:
    print('O valor {} em Octal é: {}'.format(numero, oct(numero)[2:]))
elif resposta == 3:
    print('O valor {} em Hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('VALOR INVALIDO!')

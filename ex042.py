l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Estas medidas podem formar um triângulo!')
    if l1 == l2 == l3:
        print('Este é um triângulo EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('Este é um triângulo ESCALENO.')
    else:
        print('Este é um triângulo ISÓSCELES.')
else:
    print('Estas medidas NÃO podem formar um triângulo!')
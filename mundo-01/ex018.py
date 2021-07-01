import math
ang = float(input('Digite o ângulo que você deseja: '))
newAng = math.radians(ang)
print('O SENO do ângulo {}° é: {:.3f}'.format(ang, math.sin(newAng)))
print('O COSSENO do ângulo {}° é: {:.3f}'.format(ang, math.cos(newAng)))
print('E o TANGENTE do ângulo {}° é: {:.3f}.'.format(ang, math.tan(newAng)))

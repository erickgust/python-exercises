s = float(input('Qual seu salário? R$'))
if s > 1250:
    ns = s + (s*0.10)
    print('O novo salário após 10% de aumento será R${:.2f}'.format(ns))
else:
    ns = s + (s*0.15)
    print('O novo salário após 15% de aumento será R${:.2f}'.format(ns))

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    print(f'Com {idade} anos:', end=' ')
    if 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return 'NÃO VOTA.'
    else:
        return 'VOTO OPCIONAL.'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

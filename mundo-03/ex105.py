def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-'*30)
    media = sum(n) / len(n)
    aluno = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': media}
    if sit:
        if media >= 7:
            aluno['situação'] = 'BOA'
        elif 5 <= media < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
def media(notas_aluno: float, contador: int) -> float:
    media_notas = sum(notas_aluno)/contador
    return media_notas

def maior(notas_aluno: float) -> float:
    maior_nota = max(notas_aluno)
    return maior_nota

def menor(notas_aluno: float) -> float:
    menor_nota = min(notas_aluno)
    return menor_nota
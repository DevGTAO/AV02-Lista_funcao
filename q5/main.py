# Q5 - Controle de Notas
# Complete a questão criando o notas.py e as funções de: média, maior e menor
from notas import media, maior, menor


def main():
    notas_aluno = []
    contador = 0

    print("=== Controle de Notas ===")
    while True:
        entrada = input("Digite uma nota (ou 'sair' para encerrar): ")

        if entrada.lower() == "sair":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas_aluno.append(nota)
                contador += 1
            else:
                print("Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")

    

    if notas_aluno:
        media_notas = media(notas_aluno, contador)
        maior_nota = maior(notas_aluno)
        menor_nota = menor(notas_aluno)
        print("\n--- Resultados ---")
        print(f"Média: {media_notas:.2f}")
        print(f"Maior: {maior_nota}")
        print(f"Menor: {menor_nota}")
    else:
        print("Nenhuma nota foi informada.")


main()
# Questão 1 - Manipulação de listas e strings

def contador_palavra(frase: str, palavra: str) -> int:
    frase_minuscula = frase.lower()
    palavra_minuscula = palavra.lower()
    palavras_frase = frase_minuscula.split()
    quantidade = 0
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1
    return quantidade

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

# Quantidade de Palavras
qtd = contador_palavra(frase, palavra)
print(qtd)

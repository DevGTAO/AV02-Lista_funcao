# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções
from conversor import conversor_temperatura

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

fahrenheit = 0
celsius = 0

result = conversor_temperatura(opcao, fahrenheit, celsius)
print(result)
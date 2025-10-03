def conversor_temperatura(opcao, fahrenheit, celsius):
    result = 0
    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        result = fahrenheit
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        result = celsius
    else:
        print("Opção inválida.")
    return result
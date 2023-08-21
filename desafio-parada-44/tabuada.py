# Passo 1: Definir os números da tabuada
numeros_tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Passo 2: Loop para percorrer os números da tabuada
for numero in numeros_tabuada:

    print(f"Tabuada do {numero}:")

    # Passo 3: Loop para percorrer os números de 1 a 10
    for multiplicador in range(1, 11):
        # Passo 4: Multiplicar o número da tabuada pelo multiplicador e mostrar o resultado
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

    print()  # Pula uma linha para separar as tabuadas

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

# Solicitar um número do usuário
num = int(input("Digite um número para calcular o fatorial: "))

# Chamar a função e imprimir o resultado
resultado = calcular_fatorial(num)
print(f"O fatorial de {num} é {resultado}")

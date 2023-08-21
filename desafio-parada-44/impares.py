# Passo 1: Pedir ao usuário para digitar um número
numero_usuario = int(input("Digite um número: "))

print(f"Números ímpares até {numero_usuario}:")  # Mostra a mensagem na tela

# Passo 2: Loop para percorrer os números até o número digitado pelo usuário
for numero in range(1, numero_usuario + 1):
    
    # Passo 3: Verificar se o número é ímpar
    if numero % 2 != 0:  # O resto da divisão por 2 é diferente de 0 (ímpar)
        print(numero)  # Imprime o número ímpar

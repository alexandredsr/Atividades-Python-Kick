tipo = input("Digite 'quadrado' para calcular a área de um quadrado ou 'retangulo' para calcular a área de um retângulo: ")
if tipo == 'quadrado':
    lado = float(input("Digite o valor do lado do quadrado: "))
    area = lado * lado
    print("A área do quadrado é:", area)
elif tipo == 'retangulo':
    base = float(input("Digite o valor da base do retângulo: "))
    altura = float(input("Digite o valor da altura do retângulo: "))
    area = base * altura
    print("A área do retângulo é:", area)
else:
    print("Opção inválida.")

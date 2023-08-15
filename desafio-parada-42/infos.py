# Inicializa listas vazias para armazenar informações dos produtos
codigos = []
nomes = []
quantidades = []
precos = []

# Solicita ao usuário quantos produtos deseja cadastrar
num_produtos = int(input("Quantos produtos você deseja cadastrar? "))

# Loop para cadastrar as informações dos produtos
for i in range(num_produtos):
    print(f"\nCadastro do produto {i+1}:")
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade do produto: "))
    preco = float(input("Preço do produto: "))
    
    # Armazena as informações nas listas
    codigos.append(codigo)
    nomes.append(nome)
    quantidades.append(quantidade)
    precos.append(preco)

# Exibe as informações cadastradas
print("\nInformações dos produtos cadastrados:")
for i in range(num_produtos):
    print(f"Produto {i+1}:")
    print(f"Código: {codigos[i]}")
    print(f"Nome: {nomes[i]}")
    print(f"Quantidade: {quantidades[i]}")
    print(f"Preço: R${precos[i]:.2f}")
    print()

# Calcula o valor total da compra
valor_total = sum(quantidades[i] * precos[i] for i in range(num_produtos))
print(f"Valor total da compra: R${valor_total:.2f}")

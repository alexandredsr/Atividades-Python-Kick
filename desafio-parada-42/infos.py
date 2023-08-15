produto1_nome = input("Digite o nome do primeiro produto: ")
produto1_preco = float(input("Digite o preço do primeiro produto: "))
produto2_nome = input("Digite o nome do segundo produto: ")
produto2_preco = float(input("Digite o preço do segundo produto: "))
preco_total = produto1_preco + produto2_preco
print("Produtos cadastrados:")
print("Produto 1: {} - Preço: R${:.2f}".format(produto1_nome, produto1_preco))
print("Produto 2: {} - Preço: R${:.2f}".format(produto2_nome, produto2_preco))
print("Preço total: R${:.2f}".format(preco_total))

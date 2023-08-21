def funcao():
    mensagens = []
    for _ in range(5):
        mensagens.append("hello")
    return mensagens

mensagens = funcao()
print(" ".join(mensagens))

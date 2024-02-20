import os
# importei o os que é uma variavel reservada cheia de funcoes

mensagens = []

nome = input("Nome: ")

while True:
    # IMPORTANTE o espacamento importa em python, caso seja mal organizado o codigo não funciona

    # limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_______________")

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })

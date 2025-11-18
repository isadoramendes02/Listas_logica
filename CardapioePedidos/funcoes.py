from tabulate import tabulate

def carregar_cardapio():
    return [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
        {"id": 2, "nome": "Pizza", "preco": 30},
        {"id": 3, "nome": "Refrigerante", "preco": 5}
    ]


def exibir_cardapio(cardapio):
    tabela = []
    for item in cardapio:
        tabela.append([item["id"], item["nome"], f"R$ {item['preco']}"])

    print(tabulate(tabela, headers=["ID", "Item", "Preço"], tablefmt="grid"))


def adicionar_pedido(cardapio, pedido):
    id_item = int(input("ID do item: "))
    quantidade = int(input("Quantidade: "))

    for item in cardapio:
        if item["id"] == id_item:
            pedido.append({
                "id": id_item,
                "item": item["nome"],
                "quantidade": quantidade,
                "total": item["preco"] * quantidade
            })
            print("Item adicionado!")
            return

    print("ID não encontrado.")


def exibir_pedido(pedido):
    if not pedido:
        print("Nenhum item no pedido.")
        return

    tabela = []
    total_geral = 0

    for p in pedido:
        tabela.append([p["item"], p["quantidade"], f"R$ {p['total']}"])
        total_geral += p["total"]

    print(tabulate(tabela, headers=["Item", "Qtd", "Total"], tablefmt="grid"))
    print(f"TOTAL GERAL: R$ {total_geral}")


def remover_item(pedido):
    nome = input("Nome do item para remover: ")

    for p in pedido:
        if p["item"].lower() == nome.lower():
            pedido.remove(p)
            print("Item removido!")
            return

    print("Item não encontrado.")
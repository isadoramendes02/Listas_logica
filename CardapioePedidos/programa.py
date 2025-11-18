from funcoes import *

cardapio = carregar_cardapio()
pedido = []

while True:
    print("\n1-Cardápio | 2-Adicionar | 3-Pedido | 4-Remover | 0-Sair")
    opcao = int(input("Escolha: "))
    
    if opcao == 1:
        print("\n--- CARDÁPIO ---")
        exibir_cardapio(cardapio)

    elif opcao == 2:
        adicionar_pedido(cardapio, pedido)

    elif opcao == 3:
        print("\n--- PEDIDO ---")
        exibir_pedido(pedido)

    elif opcao == 4:
        remover_item(pedido)

    elif opcao == 0:
        print("Finalizado! Obrigada pela preferência!")
        break
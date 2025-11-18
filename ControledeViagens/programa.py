from funcoes import *

listaViagens = []

while True:
    print("""
---------------MENU-----------------
1 - Registrar nova viagem           |
2 - Exibir todas as viagens         |
3 - Buscar viagens por motorista    |
4 - Exibir viagem mais cara         |
5 - Mostrar média geral de consumo  |
0 - Sair                            |
------------------------------------  """)
    
    try:
        opcao = int(input("Escolha uma opcão: "))
    except ValueError:
        print("/n Opção inválida! Digite um número./n")
        

    if opcao == 1:
        registrar_viagem(listaViagens)
    elif opcao == 2:
        exibir_viagens(listaViagens)
    elif opcao == 3:
        buscar_motorista(listaViagens)
    elif opcao == 4:
        viagem_mais_cara(listaViagens)
    elif opcao == 5:
        media_consumo(listaViagens)
    elif opcao == 0:
        print("/n Encerrando o programa. Até logo!/n")
        break
    else:
        print("/n Opção inválida! Tente novamente./n")


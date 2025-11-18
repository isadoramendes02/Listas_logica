from funcoes import *

listaLivros = []

while True:
    print("BIBLIOTECA PYTHON")
    print("1- Adicionarlivro")
    print("2- Exibir todos os livros")
    print("3- Emprestar livro")
    print("4- Devolver livro")
    print("0- Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        print(adicionar_livro(listaLivros))
    elif opcao == "2":
        print(exibir_livros(listaLivros))
    elif opcao == "3":
        print(emprestar_livro(listaLivros))
    elif opcao == "4":
        print(devolver_livro(listaLivros))
    elif opcao == "0":
        print(Fore.MAGENTA + "Saindo... até logo!")
        break
    else:
        print("Fore,RED + Opção invalida")

    
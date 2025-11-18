from tabulate import tabulate
from colorama import Fore, Style, init

init (autoreset=True)

def adicionar_livro(listaLivros):
    titulo = input("Digite um titulo:")
    autor = input("Digite um autor:")
    status = "DISPONIVEL"
    livro = {"titulo":titulo, "autor":autor, "status":"disponível"}
    listaLivros.append(livro)
    return " Fore.GREEN + Livro adicionado com sucesso!"
def formatar_tabela(listaLivros):
    tabela = []

    for i, livro in enumerate (listaLivros):
        status = (
            Fore.GREEN + "DISPONIVEL"
            if livro["status"] == "DISPONIVEL"
            else Fore.RED + "EMPRESTADO"
        )
    tabela.append([i + 1, livro["titulo"], livro["autor"], status])    

    return tabulate(
        tabela,
        headers=[Fore.YELLOW + "ID", "Titulo", "Autor", "Status"],
        tablefmt="francy_grid"
    )

def exibir_livros(listaLivros):
    if not listaLivros:
        return "Nenhum livro cadastrado ainda." 
    return "\n" + formatar_tabela (listaLivros) + "\n"
    
def emprestar_livro(listaLivros):
    if not listaLivros:
        return Fore.YELLOW + "Nenhum livro emprestar."
    
    print(exibir_livros(listaLivros))
    escolha = int(input("Digite o ID do livro para emprestar:")) - 1
    if 0 <= escolha < len(listaLivros):
        if listaLivros [escolha] ["status"] == "disponivel":
            listaLivros [escolha]["status"] = "emprestado"
            return Fore.RED + "livro emprestado"
        return Fore.YELLOW + "Esse livro já está emprestado"
    
    return Fore.RED + "ID invalido"
        
def devolver_livro(listaLivros):
    if not listaLivros:
        return Fore.YELLOW + "Nenhum livro para devolver"
    
    print(exibir_livros(listaLivros))
    escolha = int(input("Digite o ID do livro para devolver:")) -1

    if 0 <= escolha < len (listaLivros):
        if listaLivros [escolha]["status"] == "emprestado":
            listaLivros [escolha]["status"] = "disponível"
            return Fore.GREEN + "ivro devolvido!"
        return Fore.YELLOW + "Esse livro já está disponivel!"
    
    return Fore.RED + "ID invalido!"
    
 

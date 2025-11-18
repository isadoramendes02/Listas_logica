from funcoes import *
from tabulate import tabulate
from colorama import just_fix_windows_console
just_fix_windows_console()


alunos = []


while True:
    cadastro = int(input("Escolha uma opção: 1 - Cadastrar aluno e notas; 2 - Exibir relatório; 0 - Sair: "))


    if cadastro == 1:
        nome_aluno = input("Digite o nome do aluno: ")
       
        media = calcular_media()
        situacao = verificar_situacao(media)
        alunos.append({
            "nome": nome_aluno,
            "media": media,
            "situacao": situacao
        })


        print(f"\nAluno(a) {nome_aluno} cadastrado(a) com sucesso!\n")


    elif cadastro == 2:
        print("\n=== RELATÓRIO DE ALUNOS ===")
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado ainda.\n")
        else:
            tabela = []
            for aluno in alunos:
                tabela.append([aluno["nome"], f"{aluno['media']:.2f}", aluno["situacao"]])
            print(tabulate(tabela, headers=["Nome", "Média", "Situação"], tablefmt="grid"))
            print()


    elif cadastro == 0:
        print("Saindo do sistema...")
        break


    else:
        print("Opção inválida. Tente novamente.\n")



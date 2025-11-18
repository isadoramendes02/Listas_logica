def calcular_media():
    listaNotas = []
    qntd_de_notas = int(input("De quantas notas você deseja calcular a média: "))
    for i in range(qntd_de_notas):
        nota = float(input(f"Digite a nota {i+1}: "))
        listaNotas.append(nota)
    media = sum(listaNotas) / len(listaNotas)
    return media

def verificar_situacao(media):
    if media >= 7:
        return "Você está aprovado, parabéns!"
    elif 5 <= media < 7:
        return "Recuperação..."
    else:
        return "Você está reprovado, estude mais..."

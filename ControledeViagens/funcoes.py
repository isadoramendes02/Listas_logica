from tabulate import tabulate

def registrar_viagem(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("Qual o seu destino?: ")
    distancia = float (input("Qual a distância percorrida (em km)?: "))
    gasto = float(input("Qual o valor gasto em combustível (em R$)?: "))
    consumo = gasto / distancia

    viagem = {
        "motorista": motorista,
        "destino": destino,
        "distancia": distancia,
        "gasto": gasto,
        "consumo": consumo
    }

    listaViagens.append(viagem)
    return listaViagens


def exibir_viagens(listaViagens):
    if not listaViagens:
        return"/n Não há viagem cadastrada!/n"
        
    
    tabela = []
    for v in listaViagens:
        tabela.append([
            v["motorista"],
            v["destino"],
            f"{v['distancia']} km",
            f"R$ {v['gasto']}",
            f"R$ {v['consumo']:.2f}/km"
    ])  

    print("/n Viagens Registradas:/n")
    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo Médio "], tablefmt="grid"))
    print()  


def buscar_motorista(listaViagens):
    nome = input("Digite o nome do motorista: ")
    viagens_motorista = [v for v in listaViagens if v["motorista"]]

    if not viagens_motorista:
        print("/n Nenhuma viagem encontrada para esse motorista./n")
        return
    
    tabela = []
    for v in viagens_motorista:
        tabela.append([
            v["motorista"],
            v["destino"],
            f"{v['distancia']} km",
            f"R$ {v['gasto']:.2f}",
            f"R$ {v['consumo']:.2f}/km"
        ])

    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo Médio"], tablefmt="grid"))
    print()  


def viagem_mais_cara(listaViagens):
    if not listaViagens:
        return "/n Nenhuma viagem registrada. /n"  
           
    
    mais_cara = max(listaViagens, key=lambda v: v["gasto"])
    print("/n Viagem mais cara:")
    print(f"Motorista: {mais_cara['motorista']}")
    print(f"Destino: {mais_cara['destino']}")
    print(f"Gasto: R$ {mais_cara['gasto']:.2f}/n")


def media_consumo(listaViagens):
    if not listaViagens:
        return"/n Nenhuma viagem registrada./n"
        
        
    media = sum(v["consumo"] for v in listaViagens) / len(listaViagens)
    print(f"/n Média geral de consumo: R$ {media :.2f}/km/n")
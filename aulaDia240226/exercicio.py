listaDeFrequencia = []

def coletarInformacoes():

    while True:
        frequencia = input("Qual elevador você utiliza com mais frequência: A, B ou C? ").strip().upper()
        periodo = input("Em qual período você mais utiliza ele: Manhã(M), Tarde(V) ou Noite(N)? ").strip().upper()


        if not frequencia or not periodo:
            print("Não pode deixar valores vazios!\n")
            continue

        frequencia = frequencia[0]
        periodo = periodo[0]

        if frequencia not in "ABC" or periodo not in "MVN":
            print("Informações inseridas de forma incorreta!\n")
            continue

        salvarNaLista(frequencia, periodo)
        break

    qc = input("Deseja continuar? [S/N] ").strip().upper()
    return qc


def salvarNaLista(frequencia, periodo):
    informacaoJunta = frequencia + periodo
    listaDeFrequencia.append(informacaoJunta)


def realizarCalculos():

    contElevador = {"A": 0, "B": 0, "C": 0}
    contPeriodo = {"M": 0, "V": 0, "N": 0}
    contElevadorPeriodo = {}


    for item in listaDeFrequencia:
        elevador = item[0]
        periodo = item[1]

        contElevador[elevador] += 1
        contPeriodo[periodo] += 1

        chave = item
        if chave not in contElevadorPeriodo:
            contElevadorPeriodo[chave] = 0
        contElevadorPeriodo[chave] += 1

    elevadorMaisUsado = max(contElevador, key=contElevador.get)
    elevadorPeriodoMaisUsado = max(contElevadorPeriodo, key=contElevadorPeriodo.get)


    periodoMaisUsado = max(contPeriodo, key=contPeriodo.get)


    maior = max(contPeriodo.values())
    menor = min(contPeriodo.values())

    if maior == 0:
        diferenca = 0
    else:
        diferenca = ((maior - menor) / maior) * 100

    print("\n===== RESULTADOS =====")
    print(f"Elevador mais utilizado: {elevadorMaisUsado}")
    print(f"Maior fluxo concentrado em: Elevador {elevadorPeriodoMaisUsado[0]} no período {elevadorPeriodoMaisUsado[1]}")
    print(f"Período mais utilizado: {periodoMaisUsado}")
    print(f"Diferença percentual entre mais usado e menos usado: {diferenca:.2f}%")


def rodarPrograma():
    while True:
        qc = coletarInformacoes()
        if qc == "N":
            break

    realizarCalculos()

rodarPrograma()

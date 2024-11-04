import json
import random
import sys
import os
os.system("")


utr_pedidos = 3
COLOR = {
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "ENDC": "\033[0m",
}

#  o arquivo ifood_turno simula uma base de dados
with open('ifood_turno.json', 'r') as arquivo:
    motoboys = json.load(arquivo)


def obter_qtd_motoboys(horario_demanda, pedidos_demanda):
    if len(motoboys) == 0:
        return pedidos_demanda // utr_pedidos
    else:
        motoboys_disponiveis = []
        qtd_motoboys_disponiveis = 0
        #  varre nossa base de dados em busca de motoboys cadastrados dentro do período informado
        for motoboy in motoboys:
            if horario_demanda >= motoboy['hora_inicio_turno'] and horario_demanda <= motoboy['hora_fim_turno']:
                qtd_motoboys_disponiveis += 1
                motoboys_disponiveis.append(motoboy)

        if qtd_motoboys_disponiveis > 0:
            print(f"Já existe(m) " + str(qtd_motoboys_disponiveis) + " motoboy(s) cadastrados que contemplam este período. Lista: ")
            for motoboy in motoboys_disponiveis:
                print(COLOR["BLUE"], f"Nome: {motoboy["nome"]} | Início Turno: {motoboy["hora_inicio_turno"]}h | Fim Turno: {motoboy["hora_fim_turno"]}h", COLOR["ENDC"])

            resposta = input("Deseja continuar? (s/n): ")
            if resposta.lower() == 'n': 
                sys.exit()
            else:
                return qtd_motoboys_disponiveis
        else:
            return pedidos_demanda // utr_pedidos


def add_motoboy(nome, hora_inicio, tempo_turno, pedidos_demanda):
    motoboy = {
        "nome": nome,
        "hora_inicio_turno": hora_inicio,
        "hora_fim_turno": (hora_inicio + tempo_turno) - 1,
        "qtd_pedidos": pedidos_demanda
    }
    motoboys.append(motoboy)
    with open('ifood_turno.json', 'w') as turnos:
        json.dump(motoboys, turnos, indent=4)


if __name__ == "__main__":
    horario_demanda = int(input("Qual é o horário da demanda?  "))
    pedidos_demanda = int(input("Quantos pedidos a demanda possui?  "))

    qtd_motoboys = obter_qtd_motoboys(horario_demanda, pedidos_demanda)

    print(COLOR["BLUE"], f"Você irá precisar de " + str(qtd_motoboys) + " motoboy(s)!", COLOR["ENDC"])

    for i in range(qtd_motoboys):
        codigo_motoboy = random.randint(1, 100)
        tempo_turno = int(input("Quanto tempo de turno para o motoboy " + str(i+1) + "?  "))
        add_motoboy("Motoboy IFOOD-00" + str(codigo_motoboy), horario_demanda, tempo_turno, pedidos_demanda)
        print(COLOR["GREEN"], f"Motoboy cadastrado!", motoboys, COLOR["ENDC"])
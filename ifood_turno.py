import json
import random
import os
os.system("")


utr_pedidos = 3
COLOR = {
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "ENDC": "\033[0m",
}

with open('ifood_turno.json', 'r') as arquivo:
    motoboys = json.load(arquivo)  # carrega o conteúdo do arquivo em um dicionário Python


def obter_qtd_motoboys(horario_demanda, pedidos_demanda):
    if len(motoboys) == 0:
        return pedidos_demanda // utr_pedidos
    else:
        motoboys_disponiveis = 0
        for motoboy in motoboys:
            if horario_demanda >= motoboy['hora_inicio_turno'] and horario_demanda <= motoboy['hora_fim_turno']:
                motoboys_disponiveis += 1

        if motoboys_disponiveis > 0:
            return motoboys_disponiveis
        else:
            return pedidos_demanda // utr_pedidos


def add_motoboy(nome, hora_inicio, fim_turno):
    motoboy = {
        "nome": nome,
        "hora_inicio_turno": hora_inicio,
        "hora_fim_turno": (hora_inicio + fim_turno) - 1
    }
    motoboys.append(motoboy)
    with open('ifood_turno.json', 'w') as turnos:
        json.dump(motoboys, turnos, indent=4)


if __name__ == "__main__":
    horario_demanda = int(input("Qual é o horário da demanda?  "))
    pedidos_demanda = int(input("Quantos pedidos a demanda possui?  "))

    qtd_motoboys = obter_qtd_motoboys(horario_demanda, pedidos_demanda)

    print(COLOR["BLUE"], "Você irá precisar de " + str(qtd_motoboys) + " motoboy(s)!", COLOR["ENDC"])

    for i in range(qtd_motoboys):
        codigo_motoboy = random.randint(1, 100)
        tempo_turno = int(input("Quanto tempo de turno para o motoboy " + str(i+1) + "?  "))
        add_motoboy("Motoboy IFOOD-00" + str(codigo_motoboy), horario_demanda, tempo_turno)
        print(COLOR["GREEN"], "Motoboy cadastrado!", motoboys, COLOR["ENDC"])
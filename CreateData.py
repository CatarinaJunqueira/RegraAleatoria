import numpy as np

def CreateData(data):
    C = data['C'][0][0]
    R = data['R'][0][0]
    Navio = np.zeros((R, C))
    Patios = data['Patios'].tolist()
    Npatios = len(Patios)
    P = Npatios + 1  # numero de portos
    for add in range(Npatios):  # corrigindo a quantidade de posicoes vazias nos patios
        if Patios[add][0].shape[0] * Patios[add][0].shape[1] - np.count_nonzero(Patios[add][0]) < Patios[add][0].shape[
            0] - 1:
            # se o numero de posicoes livres for menor do que o numero de uma coluna - 1
            # adicionar uma linha de zeros no topo do patio
            Patios[add][0] = np.vstack([np.zeros((1, Patios[add][0].shape[1])), Patios[add][0]])
    phi = data['phi'].tolist()

    for o in range(Npatios):
        for d in range(P):
            if phi[o][d].shape[1] != 0:
                phi[o][d] = phi[o][d].tolist()[0]
            else:
                phi[o][d] = []

    return Patios, phi, Navio

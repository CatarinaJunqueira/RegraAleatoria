import numpy as np
from scipy.io import loadmat
import pandas as pd


def SimulaRegras(porto, Patio, Navio, porto_dict, Rr, Rc, Rd):

    MovGeral = 0

    if porto == 0:
        Navio, N_Rem = eval(Rr)(Patio, Navio, porto_dict, Rc)
        MovGeral += N_Rem
    else:
        if porto + 1 in porto_dict.values():
            # verificar se ha conteineres para serem desembarcados neste porto. Se nao houver, ir direto para o carregamento
            Navio, N_Rem = eval(Rd)(Navio, porto_dict, porto + 1, Rr, Rc)
            MovGeral += N_Rem
            Navio, N_Rem = eval(Rr)(Patio, Navio, porto_dict, Rc)
            MovGeral += N_Rem
        else:
            Navio, N_Rem = eval(Rr)(Patio, Navio, porto_dict, Rc)
            MovGeral += N_Rem

    return MovGeral


def Rr1(Patio, Navio, porto_dict, Rc):  # Por linha, de baixo para cima, da esquerda para a direita

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for ii in range(L - 1, -1, -1):
                    if flag == 1:
                        break
                    for jj in range(C):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio


    return Navio, N_Rem


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr2(Patio, Navio, porto_dict, Rc):  # Por coluna, de baixo para cima, da esquerda para a direita

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for jj in range(C):
                    if flag == 1:
                        break
                    for ii in range(L - 1, -1, -1):  # de baixo para cima, da esquerda para a direita
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr3(Patio, Navio, porto_dict, Rc):  # por linha, da direita para a esquerda

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for ii in range(L - 1, -1, -1):
                    if flag == 1:
                        break
                    for jj in range(C - 1, -1, -1):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr4(Patio, Navio, porto_dict, Rc):  # por coluna, da direita para esquerda

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for jj in range(C - 1, -1, -1):  # coluna, direita para esquerda
                    if flag == 1:
                        break
                    for ii in range(L - 1, -1, -1):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr5(Patio, Navio, porto_dict, Rc):  # Por linha, intercalando as linhas

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0  # flag para sair do loop
                for ii in range(L - 1, -1, -1):  # linhas de baixo para cima
                    if flag == 1:
                        break
                    if ii % 2 == 0:  # flag para inverter o sentido da linha
                        a = 0
                        b = C
                        passo = 1
                    else:
                        a = C - 1
                        b = -1
                        passo = -1
                    for jj in range(a, b, passo):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr6(Patio, Navio, porto_dict, Rc):  # Por linha, intercalando as linhas, 2

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0  # flag para sair do loop
                for ii in range(L - 1, -1, -1):  # linhas de baixo para cima
                    if flag == 1:
                        break
                    if ii % 2 != 0:  # flag para inverter o sentido da linha
                        a = 0
                        b = C
                        passo = 1
                    else:
                        a = C - 1
                        b = -1
                        passo = -1
                    for jj in range(a, b, passo):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr7(Patio, Navio, porto_dict, Rc):  # Caserta - prioridades por coluna

    P = Patio.max()
    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                prioridades = np.zeros((1, C))
                Aux = np.count_nonzero(Patio, axis=0)
                for n in range(C):
                    if Aux[n] != L:  # se a coluna nao estah cheia
                        if n != j:  # se nao eh a mesma coluna do conteiner que vai sair
                            if Aux[n] == 0:  # se a coluna eh vazio
                                prioridades[0, n] = P + 1
                            else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])

                temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                    _, jj = np.where(Patio == max(max(prioridades)))
                    ii = np.nonzero(Patio[:, int(jj)])[0]
                    Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                    N_Rem += 1
                else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                    _, jj = np.where(Patio == min(temp))
                    if len(jj) == 0:
                        for n in range(C):
                            if Aux[n] == 0:
                                jj = n
                                ii = L - 1
                                Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                break
                    else:
                        ii = np.nonzero(Patio[:, int(jj)])[0]
                        Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                    N_Rem += 1

            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio

            # carregar no navio

    print(N_Rem)

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr8(Patio, Navio, porto_dict, Rc):  # Caserta - prioridades por coluna + 1 cleaning move

    P = Patio.max()
    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio
    c_aux = -1
    N_Rem_aux = 0

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            if c_aux + 1 == c:  # verificando se o remanejamento anterior gerou um remanejamento na retirada seguinte...
                i2, j2 = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
                i2 = int(i2)
                j2 = int(j2)
                index_mover_aux2 = np.nonzero(Patio[:i2, j2])[
                    0]  # salvando quantos conteineres tem acima do conteiner seguinte a sair
                if len(index_mover_aux2) > len(index_mover_aux):
                    # c_aux = c       # remanejar primeiro o conteiner seguinte a sair
                    # c = c-1
                    Patio = aux.copy()
                    N_Rem -= N_Rem_aux
                    N_Rem_aux = 0
                    index_mover = np.nonzero(Patio[:i, j])[
                        0]  # identificar as linhas que tem conteineres acima bloqueando.
                    for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                        # buscar um local vazio:
                        prioridades = np.zeros((1, C))
                        Aux = np.count_nonzero(Patio, axis=0)
                        for n in range(C):
                            if Aux[
                                n] != L:  # se nao eh a mesma coluna do conteiner que vai sair ou a coluna nao estah cheia
                                if n != j:
                                    if Aux[n] == 0:  # se a coluna eh vazio
                                        prioridades[0, n] = P + 1
                                    else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                        prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])

                        temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                        if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                            _, jj = np.where(Patio == max(max(prioridades)))
                            ii = np.nonzero(Patio[:, int(jj)])[0]
                            Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                        else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                            _, jj = np.where(Patio == min(temp))
                            if len(jj) == 0:
                                for n in range(C):
                                    if Aux[n] == 0:
                                        jj = n
                                        ii = L - 1
                                        Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                        break
                            else:
                                ii = np.nonzero(Patio[:, int(jj)])[0]
                                Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                    # --------------------------------------------------------------------------------------------------#
                    # remanejado os conteineres que estavam acima do conteiner c (se houver algum), remaneja-lo
                    prioridades = np.zeros((1, C))
                    Aux = np.count_nonzero(Patio, axis=0)
                    for n in range(C):
                        if Aux[n] != L:  # se a coluna nao estah cheia
                            if n != j:  # se nao eh a mesma coluna do conteiner que vai sair
                                if Aux[n] == 0:  # se a coluna eh vazia
                                    prioridades[0, n] = P + 1
                                else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                    prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])
                    temp = prioridades[prioridades > c]
                    if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                        _, jj = np.where(Patio == max(max(prioridades)))
                        ii = np.nonzero(Patio[:, int(jj)])[0]
                        Patio[ii[0] - 1][jj] = Patio[i][j]  # mover
                        Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                        Patio[i][j] = 0  # zera a posicao antiga
                        N_Rem += 1
                    else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                        _, jj = np.where(Patio == min(temp))
                        if len(jj) == 0:
                            for n in range(C):
                                if Aux[n] == 0:
                                    jj = n
                                    ii = L - 1
                                    Patio[ii][jj] = Patio[i][j]  # mover
                                    Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                                    Patio[i][j] = 0  # zera a posicao antiga
                                    break
                        else:
                            ii = np.nonzero(Patio[:, int(jj)])[0]
                            Patio[ii[0] - 1][jj] = Patio[i][j]  # mover
                            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                            Patio[i][j] = 0  # zera a posicao antiga
                        N_Rem += 1

                    # --------------------------------------------------------------------------------------------------#
                    # remanejado c, agora retirar o conteinecer c-1 (e remanejar quem estiver em cima dele):
                    i, j = np.where(Patio == c - 1)  # localizando posicao do conteiner a ser retirado
                    i = int(i)
                    j = int(j)
                    index_mover = np.nonzero(Patio[:i, j])[
                        0]  # identificar as linhas que tem conteineres acima bloqueando.
                    for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                        # buscar um local vazio:
                        prioridades = np.zeros((1, C))
                        Aux = np.count_nonzero(Patio, axis=0)
                        for n in range(C):
                            if Aux[n] != L:  # se a coluna nao estah cheia
                                if n != j:  # se nao eh a mesma coluna do conteiner que vai sair
                                    if Aux[n] == 0:  # se a coluna eh vazio
                                        prioridades[0, n] = P + 1
                                    else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                        prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])
                        temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                        if len(
                                temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                            _, jj = np.where(Patio == max(max(prioridades)))
                            ii = np.nonzero(Patio[:, int(jj)])[0]
                            Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                        else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                            _, jj = np.where(Patio == min(temp))
                            if len(jj) == 0:
                                for n in range(C):
                                    if Aux[n] == 0:
                                        jj = n
                                        ii = L - 1
                                        Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                        break
                            else:
                                ii = np.nonzero(Patio[:, int(jj)])[0]
                                Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                    Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                    Patio[i][j] = 0  # remover o conteiner do patio

                    # --------------------------------------------------------------------------------------------------#
                    # Retirado o c-1, agora retirar o c:
                    i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
                    i = int(i)
                    j = int(j)

                    if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
                        Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                        Patio[i][j] = 0
                        # carregar no navio

                    else:  # caso contrário...
                        index_mover = np.nonzero(Patio[:i, j])[
                            0]  # identificar as linhas que tem conteineres acima bloqueando.
                        for c_rmj in range(
                                len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                            # buscar um local vazio:
                            prioridades = np.zeros((1, C))
                            Aux = np.count_nonzero(Patio, axis=0)
                            for n in range(C):
                                if Aux[n] != L:  # se a coluna nao estah cheia
                                    if n != j:  # se nao eh a mesma coluna do conteiner que vai sair
                                        if Aux[n] == 0:  # se a coluna eh vazio
                                            prioridades[0, n] = P + 1
                                        else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                            prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])

                            temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                            if len(
                                    temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                                _, jj = np.where(Patio == max(max(prioridades)))
                                ii = np.nonzero(Patio[:, int(jj)])[0]
                                Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                N_Rem += 1
                            else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                                _, jj = np.where(Patio == min(temp))
                                if len(jj) == 0:
                                    for n in range(C):
                                        if Aux[n] == 0:
                                            jj = n
                                            ii = L - 1
                                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                            break
                                else:
                                    ii = np.nonzero(Patio[:, int(jj)])[0]
                                    Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                N_Rem += 1
                        Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                        Patio[i][j] = 0  # remover o conteiner do patio
                    # --------------------------------------------------------------------------------------------------#
                    # --------------------------------------------------------------------------------------------------#
            else:  # se o remanejamento anterior nao gerou um remanejamento na retirada seguinte...

                # --------------------------------------------#
                i2, j2 = np.where(Patio == c + 1)  # localizando posicao do proximo conteiner a ser retirado
                i2 = int(i2)
                j2 = int(j2)
                index_mover_aux = np.nonzero(Patio[:i2, j2])[
                    0]  # salvando quantos conteineres tem acima do conteiner seguinte a sair
                c_aux = c
                aux = Patio.copy()
                # --------------------------------------------#

                index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
                for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                    # buscar um local vazio:
                    prioridades = np.zeros((1, C))
                    Aux = np.count_nonzero(Patio, axis=0)
                    for n in range(C):
                        if Aux[n] != L:  # se nao eh a mesma coluna do conteiner que vai sair ou a coluna nao estah cheia
                            if n != j:
                                if Aux[n] == 0:  # se a coluna eh vazio
                                    prioridades[0, n] = P + 1
                                else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                    prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])

                    temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                    if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                        _, jj = np.where(Patio == max(max(prioridades)))
                        if jj == 0:
                            raise Exception('Solucao Infactivel')
                        ii = np.nonzero(Patio[:, int(jj)])[0]
                        Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                        N_Rem += 1
                        N_Rem_aux += 1
                    else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                        _, jj = np.where(Patio == min(temp))
                        if len(jj) == 0:
                            for n in range(C):
                                if Aux[n] == 0:
                                    jj = n
                                    ii = L - 1
                                    Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                    break
                        else:
                            ii = np.nonzero(Patio[:, int(jj)])[0]
                            Patio[ii[0] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                        N_Rem += 1
                        N_Rem_aux += 1
                Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
                Patio[i][j] = 0  # remover o conteiner do patio
                # carregar no navio

    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr9(Patio, Navio, porto_dict, Rc):  # Regra da menor coluna

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                Aux = np.count_nonzero(Patio, axis=0)
                jj = np.argmin(Aux)  # coluna do menor valor em Aux # Only the first occurrence is returned.
                int(jj)
                if jj == j:  # se eh a mesma coluna em que o conteiner jah estah
                    Aux = np.delete(Aux, jj)
                    jj = np.argmin(Aux)
                    int(jj)
                Patio[L - Aux[jj] - 1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                N_Rem += 1
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio

    print(N_Rem)
    return Navio, N_Rem  # , Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rr10(Patio, Navio, porto_dict, Rc):  # Regra da coluna mais próxima

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0
            # carregar no navio
        else:
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                Aux = np.count_nonzero(Patio, axis=0)
                # ------------------------------------------------------------------------------------------------------#
                # ------------------------------------------------------------------------------------------------------#
                if j == C - 1:  # se o conteiner a sair estah na coluna mais a direita
                    for j_aux1 in range(j - 1, -1, -1):  # linhas de baixo para cima
                        if Aux[j_aux1] != L:  # se a coluna nao estah cheia
                            Patio[L - Aux[j_aux1] - 1][j_aux1] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            break
                # ------------------------------------------------------------------------------------------------------#
                # ------------------------------------------------------------------------------------------------------#
                if j == 0:  # se o conteiner a sair estah na coluna mais a esquerda
                    for j_aux1 in range(j + 1, C):  # linhas de baixo para cima
                        if Aux[j_aux1] != L:  # se a coluna nao estah cheia
                            Patio[L - Aux[j_aux1] - 1][j_aux1] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            break
                # ------------------------------------------------------------------------------------------------------#
                # ------------------------------------------------------------------------------------------------------#
                if 0 < j < C - 1:
                    for j_aux1 in range(j - 1, -1, -1):  # linhas de baixo para cima
                        for j_aux2 in range(j + 1, C):  # linhas de baixo para cima
                            if Aux[j_aux1] <= Aux[j_aux2]:
                                if Aux[j_aux1] != L:  # se a coluna nao estah cheia
                                    Patio[L - Aux[j_aux1] - 1][j_aux1] = Patio[index_mover[c_rmj]][j]  # mover
                                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                    N_Rem += 1
                                    break
                                else:
                                    if Aux[j_aux2] != L:  # se a coluna nao estah cheia
                                        Patio[L - Aux[j_aux2] - 1][j_aux2] = Patio[index_mover[c_rmj]][j]  # mover
                                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                        N_Rem += 1
                                        break
                            else:
                                if Aux[j_aux2] != L:  # se a coluna nao estah cheia
                                    Patio[L - Aux[j_aux2] - 1][j_aux2] = Patio[index_mover[c_rmj]][j]  # mover
                                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                    N_Rem += 1
                                    break
                                else:
                                    if Aux[j_aux1] != L:  # se a coluna nao estah cheia
                                        Patio[L - Aux[j_aux1] - 1][j_aux1] = Patio[index_mover[c_rmj]][j]  # mover
                                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                        N_Rem += 1
                                        break
            Navio = eval(Rc)(Navio, Patio[i][j], porto_dict)
            Patio[i][j] = 0  # remover o conteiner do patio

    print(N_Rem)
    return Navio, N_Rem  # , Navio


# ----------------------------------------------------------------- #
# -----------------------------------------------------------------#
# Regras do Navio:
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc1(Navio, cont, _):  # Por linha, de baixo para cima, da esquerda para a direita

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) < L * C:
            for l in range(L - 1, -1, -1):
                for c in range(C):
                    if Navio[b][l][c] != 0:
                        Navio[b][l][c] = cont
                        return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc2(Navio, cont, _):  # Por coluna, de baixo para cima, da esquerda para a direita

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) < L * C:
            for c in range(C):
                for l in range(L - 1, -1, -1):
                    if Navio[b][l][c] != 0:
                        Navio[b][l][c] = cont
                        return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc3(Navio, cont):  # por linha, da direita para a esquerda

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) < L * C:
            for l in range(L - 1, -1, -1):
                for c in range(C - 1, -1, -1):
                    if Navio[b][l][c] != 0:
                        Navio[b][l][c] = cont
                        return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc4(Navio, cont, _):  # por coluna, da direita para esquerda

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) < L * C:
            for c in range(C - 1, -1, -1):  # coluna, direita para esquerda
                for l in range(L - 1, -1, -1):
                    if Navio[b][l][c] != 0:
                        Navio[b][l][c] = cont
                        return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc5(Navio, cont, _):  # Por linha, de baixo para cima, da esquerda para a direita, intercalando as baias

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for l in range(L - 1, -1, -1):
        for c in range(C):
            for b in range(B):
                if Navio[b][l][c] != 0:
                    Navio[b][l][c] = cont
                    return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc6(Navio, cont, _):  # Por coluna, de baixo para cima, da esquerda para a direita, intercalando as baias

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for c in range(C):
        for l in range(L - 1, -1, -1):
            for b in range(B):
                if Navio[b][l][c] != 0:
                    Navio[b][l][c] = cont
                    return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc7(Navio, cont, _):  # por linha, da direita para a esquerda, intercalando as baias

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for l in range(L - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            for b in range(B):
                if Navio[b][l][c] != 0:
                    Navio[b][l][c] = cont
                    return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rc8(Navio, cont, _):  # por coluna, da direita para esquerda, intercalando as baias

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for c in range(C - 1, -1, -1):  # coluna, direita para esquerda
        for l in range(L - 1, -1, -1):
            for b in range(B):
                if Navio[b][l][c] != 0:
                    Navio[b][l][c] = cont
                    return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def Rc9(Navio, cont, porto_dict):  # This rule fills the ship matrix through a stack score based on the removal priority
    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) == 0:
            # se a baia estah inteira vazia, colocar na primeira posicao
            Navio[b][L-1][0] = cont
            return Navio
        if np.count_nonzero(Navio[b]) < L*C:
            prioridades = np.zeros((1,C)).astype(int)
            Navio_aux = np.zeros((L,C)).astype(int)
            for c in range(C):
                for l in range(L):
                    if Navio[b][l][c] != 0:
                        Navio_aux[l][c] = porto_dict[Navio[b][l][c]]
                nonzero = np.count_nonzero(Navio_aux[:, c])
                if nonzero != 0 and nonzero < L:
                    prioridades[0, c] = np.min(Navio_aux[:, c][np.nonzero(Navio_aux[:, c])])
                if nonzero == 0:
                    prioridades[0, c] = max(porto_dict.values()) + 1

            temp = prioridades[prioridades >= porto_dict[cont]]
            _, col = np.where(prioridades >= porto_dict[cont])
            if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                _, jj = np.where(Navio_aux == max(max(prioridades)))
                if len(jj) > 1:
                    jj = jj[0]
                ii = np.nonzero(Navio_aux[:, int(jj)])[0]
                Navio[b][ii[0] - 1][jj] = cont  # mover
                return Navio
            else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                _, jj = np.where(Navio_aux == min(temp))
                if len(jj) == 0:
                    Aux = np.count_nonzero(Navio[b], axis=0)
                    for n in range(C):
                        if Aux[n] == 0:
                            jj = n
                            ii = L - 1  # linha da base
                            Navio[b][ii][jj] = cont
                            return Navio
                else:
                    if len(col) > 1:
                        col = col[0]
                    ii = np.nonzero(Navio_aux[:, int(col)])[0]
                    Navio[b][ii[0] - 1][col] = cont
                    return Navio

    return Navio

# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def Rc10(Navio, cont, porto_dict):  # This rule fills the ship matrix through a stack score based on the removal priority
    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) == 0:
            # se a baia estah inteira vazia, colocar na primeira posicao
            Navio[b][L-1][0] = cont
            return Navio
        if np.count_nonzero(Navio[b]) < L*C:
            prioridades = np.zeros((1,C)).astype(int)
            Navio_aux = np.zeros((L,C)).astype(int)
            for c in range(C):
                for l in range(L):
                    if Navio[b][l][c] != 0:
                        Navio_aux[l][c] = porto_dict[Navio[b][l][c]]
                nonzero = np.count_nonzero(Navio_aux[:, c])
                if nonzero != 0 and nonzero < L:
                    prioridades[0, c] = np.min(Navio_aux[:, c][np.nonzero(Navio_aux[:, c])])
                if nonzero == 0:
                    prioridades[0, c] = max(porto_dict.values()) + 1

            temp = prioridades[prioridades >= porto_dict[cont]]
            _, col = np.where(prioridades >= porto_dict[cont])
            if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                if len(prioridades[prioridades > 0]):
                    prioridades = prioridades[prioridades > 0]
                    _, jj = np.where(Navio_aux == min(prioridades))
                else:
                    if b < B:
                        continue
                    else:
                        _, jj = np.where(Navio_aux == max(max(prioridades)))
                if len(jj) > 1:
                    jj = jj[0]
                ii = np.nonzero(Navio_aux[:, int(jj)])[0]
                Navio[b][ii[0] - 1][jj] = cont  # mover
                return Navio
            else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                _, jj = np.where(Navio_aux == min(temp))
                if len(jj) == 0:
                    Aux = np.count_nonzero(Navio[b], axis=0)
                    for n in range(C):
                        if Aux[n] == 0:
                            jj = n
                            ii = L - 1  # linha da base
                            Navio[b][ii][jj] = cont
                            return Navio
                else:
                    if len(col) > 1:
                        col = col[0]
                    ii = np.nonzero(Navio_aux[:, int(col)])[0]
                    Navio[b][ii[0] - 1][col] = cont
                    return Navio

    return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#

def Rc11(Navio, cont, _):  # Verificando qual eh a menor coluna, por baia.

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio

    for b in range(B):
        if np.count_nonzero(Navio[b]) < L*C:
            # Se ainda tem posicao disponivel na baia t para alocar o conteiner, entao coloque nesta baia:
            Aux = np.count_nonzero(Navio[b], axis=0)
            jj = np.argmin(Aux)  # coluna do menor valor em Aux # Only the first occurrence is returned.
            Navio[b][L - Aux[jj] - 1][jj] = cont
            return Navio


# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
# def Rc10(Navio, cont, _):  # Por coluna, de baixo para cima, da esquerda para a direita + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for b in range(B):
#         for c in range(C):
#             for l in range(L - 1, -1, -1):
#                 if Navio[b][l][c] != 0:
#                     if flag == 0:
#                         b_aux = b
#                         l_aux = l
#                         c_aux = c
#                         flag = 1
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                     # Se nao encontrar nenhuma posicao disponivel, colocar na primeira que encontrar
#                 Navio[b_aux][l_aux][c_aux] = cont
#                 return Navio
#
#
# # -----------------------------------------------------------------#
# # -----------------------------------------------------------------#
# def Rc11(Navio, cont, _):  # por linha, da direita para a esquerda + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for b in range(B):
#         for l in range(L - 1, -1, -1):
#             for c in range(C - 1, -1, -1):
#                 if Navio[b][l][c] != 0:
#                     if flag == 0:
#                         b_aux = b
#                         l_aux = l
#                         c_aux = c
#                         flag = 1
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                     # Se nao encontrar nenhuma posicao disponivel, colocar na primeira que encontrar
#                 Navio[b_aux][l_aux][c_aux] = cont
#                 return Navio
#
#
# # -----------------------------------------------------------------#
# # -----------------------------------------------------------------#
# def Rc12(Navio, cont, _):  # por coluna, da direita para esquerda + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for b in range(B):
#         for c in range(C - 1, -1, -1):  # coluna, direita para esquerda
#             for l in range(L - 1, -1, -1):
#                 if Navio[b][l][c] != 0:
#                     if flag == 0:
#                         b_aux = b
#                         l_aux = l
#                         c_aux = c
#                         flag = 1
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                     # Se nao encontrar nenhuma posicao disponivel, colocar na primeira que encontrar
#                 Navio[b_aux][l_aux][c_aux] = cont
#                 return Navio
#
#
# # -----------------------------------------------------------------#
# # -----------------------------------------------------------------#
# def Rc13(Navio, cont, _):  # Por linha, de baixo para cima, da esquerda para a direita, intercalando as baias + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for l in range(L - 1, -1, -1):
#         for c in range(C):
#             for b in range(B):
#                 if Navio[b][l][c] != 0:
#                     if flag == 0:
#                         b_aux = b
#                         l_aux = l
#                         c_aux = c
#                         flag = 1
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                     # Se nao encontrar nenhuma posicao disponivel, colocar na primeira que encontrar
#                 Navio[b_aux][l_aux][c_aux] = cont
#                 return Navio
#
#
# # -----------------------------------------------------------------#
# # -----------------------------------------------------------------#
# def Rc14(Navio, cont, _):  # Por coluna, de baixo para cima, da esquerda para a direita, intercalando as baias + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for c in range(C):
#         for l in range(L - 1, -1, -1):
#             for b in range(B):
#                 if Navio[b][l][c] != 0:
#                     if flag == 0:
#                         b_aux = b
#                         l_aux = l
#                         c_aux = c
#                         flag = 1
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                     # Se nao encontrar nenhuma posicao disponivel, colocar na primeira que encontrar
#                 Navio[b_aux][l_aux][c_aux] = cont
#                 return Navio
#
#
# # -----------------------------------------------------------------#
# # -----------------------------------------------------------------#
# def Rc15(Navio, cont, _):  # por linha, da direita para a esquerda, intercalando as baias + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for l in range(L - 1, -1, -1):
#         for c in range(C - 1, -1, -1):
#             for b in range(B):
#                 if Navio[b][l][c] != 0:
#                     if flag == 0:
#                         b_aux = b
#                         l_aux = l
#                         c_aux = c
#                         flag = 1
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                     # Se nao encontrar nenhuma posicao disponivel, colocar na primeira que encontrar
#                 Navio[b_aux][l_aux][c_aux] = cont
#                 return Navio
#
#
# # -----------------------------------------------------------------#
# # -----------------------------------------------------------------#
# def Rc16(Navio, cont, _):  # por coluna, da direita para esquerda, intercalando as baias + a stack score
#
#     B = len(Navio)  # numero de baias no navio
#     L = Navio[0].shape[0]  # numero de linhas no navio
#     C = Navio[0].shape[1]  # numero de colunas no navio
#     flag = 0
#
#     for c in range(C - 1, -1, -1):  # coluna, direita para esquerda
#         for l in range(L - 1, -1, -1):
#             for b in range(B):
#                 if Navio[b][l][c] != 0:
#                     if l < L:  # se nao estah no chao
#                         p = np.min(Navio[:, c][np.nonzero(Navio[:, c])])
#                         if p >= c:
#                             Navio[b][l][c] = cont
#                             return Navio
#                 else:
#                     Navio[b][l][c] = cont
#                     return Navio


# ----------------------------------------------------------------- #
# -----------------------------------------------------------------#
# Regras de descarregamento Navio:
# -----------------------------------------------------------------#
# -----------------------------------------------------------------#
def Rd1(Navio, porto_dict, P, Rr, Rc):
  # Nesta regra, quando o navio chega a um porto p, são removidos todos os
  # contêineres cujo destino é p e todos os contêineres que estão acima dos
  # contêineres do porto p e cujos destinos são os portos p+j

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio
    patio_transb = []
    N_Rem = 0

    for b in range(B):  # baia
        for l in range(L):  # linha
            for c in range(C):  # coluna
                if Navio[b][l][c] != 0 and porto_dict[Navio[b][l][c]] == P:  # se nessa posicao tem um conteiner que vai descer
                    if l != 0:  # se nao estah no topo da coluna, verificar se tem algum conteiner acima bloqueando
                        if Navio[b][l-1][c] != 0:
                            index_mover = np.nonzero(Navio[b][:l, c])[0]  # identificar as linhas que tem conteineres acima bloqueando.
                            for c_rmj in range(len(index_mover)):
                                patio_transb.append(Navio[b][index_mover[c_rmj]][c])
                                Navio[b][index_mover[c_rmj]][c] = 0
                                N_Rem += 1
                        # depois de que nao houver mais nenhum conteiner bloqueando a saida, retirar o cont objetivo
                        Navio[b][l][c] = 0
                    else:
                        Navio[b][l][c] = 0


    if len(patio_transb) != 0:
        newrow = np.zeros((len(patio_transb))).astype(int)
        arr = np.array(patio_transb)
        patio_transb = np.vstack([newrow,arr])
        Navio, num_rem = eval(Rr)(patio_transb, Navio, porto_dict, Rc)
        N_Rem += num_rem

    return Navio, N_Rem


def Rd2(Navio, porto_dict, P, Rr, Rc):
  # Retira todos os contêineres do Navio para carregá-los posteriormente
  # usando alguma regra de carregamento.

    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio
    patio_transb = []
    N_Rem = 0

    for b in range(B):  # baia
        for l in range(L):  # linha
            for c in range(C):  # coluna
                if Navio[b][l][c] != 0:
                    if porto_dict[Navio[b][l][c]] == P:  # se nessa posicao tem um conteiner que vai descer
                        Navio[b][l][c] = 0
                    else:
                        patio_transb.append(Navio[b][l][c])
                        Navio[b][l][c] = 0
                        N_Rem += 1

    if len(patio_transb) != 0:
        newrow = np.zeros((len(patio_transb))).astype(int)
        arr = np.array(patio_transb)
        patio_transb = np.vstack([newrow,arr])
        Navio, num_rem = eval(Rr)(patio_transb, Navio, porto_dict, Rc)
        N_Rem += num_rem

    return Navio, N_Rem


def Rd3(Navio, porto_dict, porto_atual, Rr, Rc):
    # Nesta regra, quando o navio chega a um porto p, são removidos todos os
    # contêineres cujo destino é p e os remanejamentos sao feitos dentro do
    # navio (na mesma baia) quando este movimento nao gere um remanejamento
    # futuro. Caso contrario eh retirado do navio e depois carregado novamente.

    P = max(porto_dict) + 1
    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio
    patio_transb = []
    N_Rem = 0

    for b in range(B):  # baia
        for l in range(L):  # linha
            for c in range(C):  # coluna
                if Navio[b][l][c] != 0 and porto_dict[Navio[b][l][c]] == porto_atual:  # se nessa posicao tem um conteiner que vai descer
                    if l != 0:  # se nao estah no topo da coluna, verificar se tem algum conteiner acima bloqueando
                        if Navio[b][l - 1][c] != 0:
                            index_mover = np.nonzero(Navio[b][:l, c])[0]  # identificar as linhas que tem conteineres acima bloqueando.
                            for c_rmj in range(len(index_mover)):
                                prioridades = np.zeros((1, C)).astype(int)
                                Aux = np.count_nonzero(Navio[b], axis=0)
                                if Aux.sum() != L*C:  # se a baia nao estah completamente cheia
                                    for n in range(C):
                                        if Aux[n] != L:  # se a coluna nao estah cheia
                                            if n != c:
                                                if Aux[n] != 0:  # se nao eh a mesma coluna do conteiner que vai sair e se a coluna nao eh vazia
                                                    # pegar o menor valor diferente de 0 dessa coluna
                                                    prioridades[0, n] = np.min(Navio[b][:, n][np.nonzero(Navio[b][:, n])])
                                                else:
                                                    prioridades[0, n] = Navio[b][index_mover[c_rmj]][c] + 1

                                        else:
                                            prioridades[0, n] = P + 1
                                else:
                                    #  nao tem onde remanejar nessa baia.
                                    patio_transb.append(Navio[b][index_mover[c_rmj]][c])
                                    Navio[b][index_mover[c_rmj]][c] = 0
                                    N_Rem += 1
                                    continue

                                temp = prioridades[(prioridades > porto_dict[Navio[b][index_mover[c_rmj]][c]]) & (prioridades < P)]
                                if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Descarregar do navio.
                                    patio_transb.append(Navio[b][index_mover[c_rmj]][c])
                                    Navio[b][index_mover[c_rmj]][c] = 0
                                    N_Rem += 1
                                    continue
                                else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                                    _, jj = np.where(Navio[b] == min(temp))
                                    if len(jj) == 0:
                                        for n in range(C):
                                            if Aux[n] == 0:
                                                jj = n
                                                ii = L - 1
                                                Navio[b][ii][jj] = Navio[b][index_mover[c_rmj]][c]  # mover
                                                Navio[b][index_mover[c_rmj]][c] = 0  # zera a posicao antiga
                                                break

                            # depois de que nao houver mais nenhum conteiner bloqueando a saida, retirar o cont objetivo
                            Navio[b][l][c] = 0
                    else:
                        Navio[b][l][c] = 0

    if len(patio_transb) != 0:
        newrow = np.zeros((len(patio_transb))).astype(int)
        arr = np.array(patio_transb)
        patio_transb = np.vstack([newrow,arr])
        Navio, num_rem = eval(Rr)(patio_transb, Navio, porto_dict, Rc)
        N_Rem += num_rem

    return Navio, N_Rem




if __name__ == '__main__':
    data = loadmat('Instancia3D-1-Tipo-1-Ocupacao-1.mat')
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]
    Navio = data['Navio'].tolist()
    Navio = Navio[0]
    B = len(Navio)  # numero de baias no navio
    L = Navio[0].shape[0]  # numero de linhas no navio
    C = Navio[0].shape[1]  # numero de colunas no navio
    aux = 1
    for l in range(L - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            for b in range(B):
                Navio[b][l][c] = aux
                aux += 1

    df = pd.DataFrame(data=data['porto'].T, columns=['porto','conteiner'])
    porto_dict = df.set_index('conteiner').to_dict()['porto']
    _ = Rd1(Navio, porto_dict, 2, Rr1)


# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr1(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr2(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr3(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr4(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr5(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr6(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr7(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr8(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr9(Patio)
# Patio = np.array([[0, 0, 5], [6, 0, 4], [7, 0, 3], [8, 2, 1]])
# _ = Rr10(Patio)
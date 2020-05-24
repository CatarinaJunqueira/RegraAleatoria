import numpy as np
from scipy.io import loadmat

#Simular a solucao representada por um individuo para ober o fitness.
#def SimulaRegras(data):


#    return fitness

def Rr1(Patio): # Por linha, de baixo para cima, da esquerda para a direita

    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i=int(i)
        j=int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for ii in range(L-1,-1,-1):
                    if flag == 1:
                        break
                    for jj in range(C):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr2(Patio):   #Por coluna, de baixo para cima, da esquerda para a direita

    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
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
                    for ii in range(L-1,-1,-1): # de baixo para cima, da esquerda para a direita
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr3(Patio): # por linha, da direita para a esquerda

    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for ii in range(L-1,-1,-1):
                    if flag == 1:
                        break
                    for jj in range(C-1,-1,-1):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr4(Patio):  # por coluna, da direita para esquerda

    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0
                for jj in range(C-1,-1,-1): # coluna, direita para esquerda
                    if flag == 1:
                        break
                    for ii in range(L-1,-1,-1):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr5(Patio): # Por linha, intercalando as linhas

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i=int(i)
        j=int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0  # flag para sair do loop
                for ii in range(L-1, -1, -1): # linhas de baixo para cima
                    if flag == 1:
                        break
                    if ii % 2 == 0:  # flag para inverter o sentido da linha
                        a = 0
                        b = C
                        passo = 1
                    else:
                        a = C-1
                        b = -1
                        passo = -1
                    for jj in range(a, b, passo):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr6(Patio): # Por linha, intercalando as linhas, 2

    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i=int(i)
        j=int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                flag = 0  # flag para sair do loop
                for ii in range(L-1, -1, -1): # linhas de baixo para cima
                    if flag == 1:
                        break
                    if ii % 2 != 0:  # flag para inverter o sentido da linha
                        a = 0
                        b = C
                        passo = 1
                    else:
                        a = C-1
                        b = -1
                        passo = -1
                    for jj in range(a, b, passo):
                        if Patio[ii][jj] == 0 and jj != j:  # se a posicao estah disponivel e nao eh na mesma coluna
                            Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                            N_Rem += 1
                            flag = 1
                            break
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio
    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr7(Patio): # Caserta - prioridades por coluna
    print(Patio)
    P = Patio.max()
    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
          print(Patio)
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                prioridades = np.zeros((1, C))
                Aux = np.count_nonzero(Patio, axis=0)
                for n in range(C):
                    if Aux[n] != L:  # se a coluna nao estah cheia
                        if n != j:   # se nao eh a mesma coluna do conteiner que vai sair
                            if Aux[n] == 0:  # se a coluna eh vazio
                                prioridades[0, n] = P+1
                            else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])

                temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                    _, jj = np.where(Patio == max(max(prioridades)))
                    ii = np.nonzero(Patio[:, int(jj)])[0]
                    Patio[ii[0]-1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                    N_Rem += 1
                else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                    _, jj = np.where(Patio == min(temp))
                    if len(jj) == 0:
                        for n in range(C):
                            if Aux[n] == 0:
                                jj = n
                                ii = L-1
                                Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                break
                    else:
                        ii = np.nonzero(Patio[:, int(jj)])[0]
                        Patio[ii[0]-1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                    N_Rem += 1

            Patio[i][j] = 0  # remover o conteiner do patio
            print(Patio)
            # carregar no navio

    print(N_Rem)

    return N_Rem #, Navio

#-----------------------------------------------------------------#
#-----------------------------------------------------------------#
def Rr8(Patio): # Caserta - prioridades por coluna + 1 cleaning move
    print(Patio)
    P = Patio.max()
    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio
    c_aux = -1
    N_Rem_aux = 0

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
          print(Patio)
           # carregar no navio

        else:  # caso contrário...
            if c_aux + 1 == c:  # verificando se o remanejamento anterior gerou um remanejamento na retirada seguinte...
                i2, j2 = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
                i2 = int(i2)
                j2 = int(j2)
                index_mover_aux2 = np.nonzero(Patio[:i2, j2])[0] # salvando quantos conteineres tem acima do conteiner seguinte a sair
                if len(index_mover_aux2) > len(index_mover_aux):
                    #c_aux = c       # remanejar primeiro o conteiner seguinte a sair
                    #c = c-1
                    Patio = aux.copy()
                    N_Rem -= N_Rem_aux
                    N_Rem_aux = 0
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
                    #--------------------------------------------------------------------------------------------------#
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
                                    Patio[i][j] = 0  # zera a posicao antiga
                                    break
                        else:
                            ii = np.nonzero(Patio[:, int(jj)])[0]
                            Patio[ii[0] - 1][jj] = Patio[i][j]  # mover
                            Patio[i][j] = 0  # zera a posicao antiga
                        N_Rem += 1

                    #--------------------------------------------------------------------------------------------------#
                    # remanejado c, agora retirar o conteinecer c-1 (e remanejar quem estiver em cima dele):
                    i, j = np.where(Patio == c-1)  # localizando posicao do conteiner a ser retirado
                    i = int(i)
                    j = int(j)
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
                    Patio[i][j] = 0  # remover o conteiner do patio

                    #--------------------------------------------------------------------------------------------------#
                    # Retirado o c-1, agora retirar o c:
                    i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
                    i = int(i)
                    j = int(j)

                    if Patio[i - 1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
                        Patio[i][j] = 0
                        print(Patio)
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

                        Patio[i][j] = 0  # remover o conteiner do patio
                    #--------------------------------------------------------------------------------------------------#
                    #--------------------------------------------------------------------------------------------------#
            else:  # se o remanejamento anterior nao gerou um remanejamento na retirada seguinte...

                #--------------------------------------------#
                i2, j2 = np.where(Patio == c + 1)  # localizando posicao do proximo conteiner a ser retirado
                i2 = int(i2)
                j2 = int(j2)
                index_mover_aux = np.nonzero(Patio[:i2, j2])[0] # salvando quantos conteineres tem acima do conteiner seguinte a sair
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
                                    prioridades[0, n] = P+1
                                else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                                    prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])

                    temp = prioridades[prioridades > Patio[index_mover[c_rmj]][j]]
                    if len(temp) == 0:  # caso em que nenhuma das prioridades eh maior do que c. Escolher a menos pior.
                        _, jj = np.where(Patio == max(max(prioridades)))
                        if jj == 0:
                            raise Exception('Solucao Infactivel')
                        ii = np.nonzero(Patio[:, int(jj)])[0]
                        Patio[ii[0]-1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                        Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                        N_Rem += 1
                        N_Rem_aux += 1
                    else:  # se satisfeita a condição, então colocar c nessa coluna não vai gerar nenhum movimento adicional.
                        _, jj = np.where(Patio == min(temp))
                        if len(jj) == 0:
                            for n in range(C):
                                if Aux[n] == 0:
                                    jj = n
                                    ii = L-1
                                    Patio[ii][jj] = Patio[index_mover[c_rmj]][j]  # mover
                                    Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                                    break
                        else:
                            ii = np.nonzero(Patio[:, int(jj)])[0]
                            Patio[ii[0]-1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                            Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                        N_Rem += 1
                        N_Rem_aux += 1

                Patio[i][j] = 0  # remover o conteiner do patio
                # carregar no navio

    print(N_Rem)

    return N_Rem #, Navio

def Rr9(Patio): # Regra da menor coluna

    N_Rem = 0 # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres > 0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                Aux = np.count_nonzero(Patio, axis=0)
                jj = np.argmin(Aux)  # coluna do menor valor em Aux # Only the first occurrence is returned.
                int(jj)
                if jj == j: # se eh a mesma coluna em que o conteiner jah estah
                    Aux = np.delete(Aux, jj)
                    jj = np.argmin(Aux)
                    int(jj)
                Patio[L-Aux[jj]-1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                N_Rem += 1
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio

    return N_Rem #, Navio

def Rr10(Patio):  # Regra da coluna mais próxima

    N_Rem = 0  # numero de remanejamentos
    conteineres = np.unique(Patio)
    conteineres = conteineres[conteineres>0].tolist()
    L = Patio.shape[0]  # numero de linhas no patio
    C = Patio.shape[1]  # numero de colunas no patio

    for c in conteineres:
        i, j = np.where(Patio == c)  # localizando posicao do conteiner a ser retirado
        i = int(i)
        j = int(j)

        if Patio[i-1][j] == 0 or i == 0:  # se nao tem nenhum conteiner bloqueando ou se eh topo
          Patio[i][j] = 0
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                Aux = np.count_nonzero(Patio, axis=0)
                jj = np.argmin(Aux)  # coluna do menor valor em Aux # Only the first occurrence is returned.
                int(jj)
                if jj == j: # se eh a mesma coluna em que o conteiner jah estah
                    Aux = np.delete(Aux, jj)
                    jj = np.argmin(Aux)
                    int(jj)
                Patio[L-Aux[jj]-1][jj] = Patio[index_mover[c_rmj]][j]  # mover
                Patio[index_mover[c_rmj]][j] = 0  # zera a posicao antiga
                N_Rem += 1
            Patio[i][j] = 0  # remover o conteiner do patio
            # carregar no navio

    print(N_Rem)

    return N_Rem #, Navio



if __name__ == '__main__':

    # data = loadmat('InstanciaModeloIntegrado_1.mat')
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]

    # _ = Rr1(Patio)
    # _ = Rr2(Patio)
    # _ = Rr3(Patio)
    # _ = Rr4(Patio)
    # _ = Rr5(Patio)
    # _ = Rr6(Patio)
    # _ = Rr7(Patio)
    #_ = Rr8(Patio)
    Patio = np.array([[0, 0, 3], [6, 0, 4], [7, 0, 5], [8, 2, 1]])
    #_ = Rr9(Patio)
    _ = Rr10(Patio)



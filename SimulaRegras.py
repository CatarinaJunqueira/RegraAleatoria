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

def Rr7(Patio): # Caserta - prioridades por coluna

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
           # carregar no navio

        else:  # caso contrário...
            index_mover = np.nonzero(Patio[:i, j])[0]  # identificar as linhas que tem conteineres acima bloqueando.
            for c_rmj in range(len(index_mover)):  # de 1 ateh a qntd de conteineres que devem ser remanejados
                # buscar um local vazio:
                prioridades = np.zeros((1, C))
                Aux = np.count_nonzero(Patio, axis=0)
                for n in range(C):
                    if n != j or Aux[n] != L:  # se nao eh a mesma coluna do conteiner que vai sair ou a coluna nao estah cheia
                        if Aux[n] == 0:  # se a coluna eh vazio
                            prioridades[0, n] = P+1
                        else:  # caso contrario, pegar o menor valor diferente de 0 dessa coluna
                            prioridades[0, n] = np.min(Patio[:, n][np.nonzero(Patio[:, n])])





                flag = 0  # flag para sair do loop
                for ii in range(L-1, -1, -1): # linhas de baixo para cima
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





if __name__ == '__main__':

    # data = loadmat('InstanciaModeloIntegrado_1.mat')
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]
    #
    # _ = Rr1(Patio)
    # data = loadmat('InstanciaModeloIntegrado_1.mat')
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]
    # _ = Rr2(Patio)
    # data = loadmat('InstanciaModeloIntegrado_1.mat')
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]
    # _ = Rr3(Patio)
    # data = loadmat('InstanciaModeloIntegrado_1.mat')
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]
    # _ = Rr4(Patio)
    data = loadmat('InstanciaModeloIntegrado_1.mat')
    Patios = data['Patios'].tolist()
    Patio = Patios[0][0]
   # _ = Rr5(Patio)
   # _ = Rr6(Patio)
    _ = Rr7(Patio)



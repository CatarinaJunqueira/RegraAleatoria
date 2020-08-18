import numpy as np
from scipy.io import loadmat
import pandas as pd
import Regras
# Simular a solucao representada por um individuo para ober o fitness.
def SimulaRegras(individuo, Patio, Navio, porto_dict):

    MovGeral = 0

    for porto in range(individuo):
        Rr, Rc, Rd = NumToRules(individuo[porto])

        if porto == 0:
            Navio, N_Rem = Rr(Patio, Navio, porto_dict, Rc)
            MovGeral += N_Rem
        else:
            if porto in porto_dict.values():
                # verificar se ha conteineres para serem desembarcados neste porto. Se nao houver, ir direto para o carregamento
                Navio, N_Rem = Rd(Navio, porto_dict, porto, Rr, Rc)
                MovGeral += N_Rem
                Navio, N_Rem = Rr(Patio, Navio, porto_dict, Rc)
                MovGeral += N_Rem
            else:
                Navio, N_Rem = Rr(Patio, Navio, porto_dict, Rc)
                MovGeral += N_Rem

    return MovGeral
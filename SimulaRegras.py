import numpy as np
from scipy.io import loadmat
import pandas as pd
import Regras
import sys

# Simular a solucao representada por um individuo para ober o fitness.
def SimulaRegras(porto, Patio, Navio, porto_dict, Rr, Rc, Rd):

    MovGeral = 0

    #for porto in range(individuo):
        #Rr, Rc, Rd = NumToRules(individuo[porto], NRr, NRc, NRd)

    if porto == 0:
        Navio, N_Rem = eval(Rr)(Patio, Navio, porto_dict, Rc)
        MovGeral += N_Rem
    else:
        if porto in porto_dict.values():
            # verificar se ha conteineres para serem desembarcados neste porto. Se nao houver, ir direto para o carregamento
            Navio, N_Rem = eval(Rd)(Navio, porto_dict, porto, Rr, Rc)
            MovGeral += N_Rem
            Navio, N_Rem = eval(Rr)(Patio, Navio, porto_dict, Rc)
            MovGeral += N_Rem
        else:
            Navio, N_Rem = eval(Rr)(Patio, Navio, porto_dict, Rc)
            MovGeral += N_Rem

    return MovGeral
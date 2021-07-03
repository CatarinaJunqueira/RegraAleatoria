import numpy as np
import pandas as pd
def CreateData(data):
    # Patios = data['Patios'].tolist()
    # Patio = Patios[0][0]
    Navio = data['Navio'].tolist()
    Navio = Navio[0]
    Navio = [np.int32(N) for N in Navio]

    p = data['patio'].tolist()
    Num_portos = len(p)

    Patios = []
    for i in range(Num_portos):
        Patios.append(p[i][0])
    Patios = [np.int32(P) for P in Patios]

    df = pd.DataFrame(data=data['porto'].T, columns=['porto','conteiner'])
    porto_dict = df.set_index('conteiner').to_dict()['porto']

    return Patios, Navio, porto_dict, Num_portos
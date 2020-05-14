from scipy.io import loadmat
import numpy as np
from CreateData import CreateData

def RegraAleatoria(casename):

    data = loadmat(casename)
    Patio, phi, Navio = CreateData(data)
    print('parametros criados')




if __name__ == "__main__":


    X = [1, 2 , 3, 5, 6, 4, 9, 10, 11, 12, 13, 14]
    #X = [7]
    for i in X:
        name_instance1 = 'InstanciaModeloIntegrado_' + str(i) + '.mat'
        print(name_instance1)
        _ = RegraAleatoria(name_instance1)
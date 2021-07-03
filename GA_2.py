import random
import copy
import matplotlib.pyplot as plt
from Regras import SimulaRegras
from scipy.io import loadmat
from CreateData import CreateData
import time
import pandas as pd
#import multiprocessing

class Produto:
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor


def NumToRules(regra_gene, NRr, NRc, NRd):
    counter = 1

    if regra_gene > NRr * NRc * NRd:
        raise Exception('Erro na função NumToRules.')

    for i in range(NRr):
        for j in range(NRc):
            for k in range(NRd):
                if counter == regra_gene:
                    Rr = 'Rr' + str(i + 1)
                    Rc = 'Rc' + str(j + 1)
                    Rd = 'Rd' + str(k + 1)
                    return Rr, Rc, Rd
                else:
                    counter += 1


class Individuo:
    def __init__(self, lbound, ubound, Num_portos, geracao=0):
        self.fitness = 0
        self.lbound = lbound
        self.ubound = ubound
        self.Num_portos = Num_portos
        self.geracao = geracao
        self.cromossomo = []
        self.conf_navio = []
        self.num_movimentos = 0

        for i in range(Num_portos):
            self.cromossomo.append(random.randint(lbound, ubound))


    def avaliacao(self, patios, navio, porto_dict, flag):
        # passar por todos os genes, simular cada um e obter o fitness final de cada individuo
        navio_vazio = copy.deepcopy(navio)
        conf_patios = copy.deepcopy(patios)
        #navio = copy.deepcopy(navio_vazio)
        fitness = 0
        my_dict = {key: 0 for key in range(len(self.cromossomo))}
        for i in range(len(self.cromossomo)):
            Rr, Rc, Rd = NumToRules(self.cromossomo[i], NRr, NRc, NRd)
            #Rc = 'Rc11'
            #Rr = 'Rr10'
            #Rd = 'Rd3'
            num_movimentos_total, navio_vazio = SimulaRegras(i, conf_patios[i], navio_vazio, porto_dict, Rr, Rc, Rd)
            fitness += num_movimentos_total
            if flag == 1:
                save_navio_vazio = copy.deepcopy(navio_vazio)
                my_dict[i] = save_navio_vazio.copy()

        self.fitness = 1/(num_movimentos_total + 1)
        self.num_movimentos = num_movimentos_total
        self.conf_navio = my_dict
        return


    def crossover(self, outro_individuo):
        corte = round(random.random() * len(self.cromossomo))

        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        filhos = [Individuo(self.lbound, self.ubound, self.Num_portos, self.geracao + 1),
                  Individuo(self.lbound, self.ubound, self.Num_portos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos

    def mutacao(self, taxa_mutacao):
        # print("Antes %s " % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random.random() < taxa_mutacao:
                self.cromossomo[i] = random.randint(lbound, ubound)

        return self


class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.num_movimentos = 0
        self.lista_solucoes = []
        self.lista_num_movimentos = []

    def inicializa_populacao(self, lbound, ubound, Num_portos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(lbound, ubound, Num_portos))
        self.melhor_solucao = self.populacao[0]

    def ordena_populacao(self):
        # ordenar do individuo com o menor para o maior numero total de movimentos
        self.populacao = sorted(self.populacao,
                                key=lambda populacao: populacao.num_movimentos,
                                reverse=False)

    def melhor_individuo(self, individuo):
        if individuo.fitness > self.melhor_solucao.fitness:
            self.melhor_solucao = individuo

    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.fitness
        return soma

    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random.random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].fitness
            pai += 1
            i += 1
        return pai

    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("Geração: %s -> Numero de Remanejamentos: %s Regra: %s" % (self.populacao[0].geracao,
                                                                         melhor.num_movimentos,
                                                                         melhor.cromossomo))

    def resolver(self, lbound, ubound, taxa_mutacao, numero_geracoes, patios, navio, porto_dict, Num_portos, tempo_inicio):
        self.inicializa_populacao(lbound, ubound, Num_portos)
        #navio_vazio = copy.deepcopy(navio)
        for individuo in self.populacao:
            individuo.avaliacao(patios, navio, porto_dict, 0)

        self.ordena_populacao()   # ordenar a populacao por numero de movimentos de cada individuo
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.fitness)
        self.lista_num_movimentos.append(self.melhor_solucao.num_movimentos)
        melhor_solucao_geracao_anterior = self.melhor_solucao.num_movimentos

        self.visualiza_geracao()

        i_contador = 0
        Flag = 0
        for geracao in range(numero_geracoes):
            if geracao == numero_geracoes - 1:
                # se a ultima geracao, salvar o navio
                Flag = 1
            soma_avaliacao = self.soma_avaliacoes()

            nova_populacao = []

            self.populacao[0].geracao +=1
            nova_populacao.append(self.populacao[0])
            for individuos_gerados in range(0, self.tamanho_populacao-1, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)

                filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))

            self.populacao = list(nova_populacao)

            for individuo in self.populacao:
                individuo.avaliacao(patios, navio, porto_dict, Flag)
            #pool.map(individuo.avaliacao(patios, navio, porto_dict, Flag), individuo in self.populacao)
            #pool.close()
            #pool.join()
            self.ordena_populacao()

            self.visualiza_geracao()

            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.fitness)
            self.lista_num_movimentos.append(self.melhor_solucao.num_movimentos)
            self.melhor_individuo(melhor)

            melhor_solucao_desta_geracao = self.melhor_solucao.num_movimentos

            if time.time() - start_time >= 3600:  # tempo limite: 1 hora
                break
            if melhor_solucao_desta_geracao >= melhor_solucao_geracao_anterior:
                i_contador += 1
                if i_contador == 15:  # numero maximo de geracoes sem melhoria na F.O.
                    break
            else:
                melhor_solucao_geracao_anterior = self.melhor_solucao.num_movimentos
                i_contador = 0


        print("\nMelhor solução -> G: %s Valor: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.num_movimentos,
               self.melhor_solucao.cromossomo))




        return self.melhor_solucao.cromossomo


if __name__ == '__main__':

    lista_FO = []
    lista_Fitness = []
    solucao = []
    num_instancias = 10
    i = 28  # instancia
    for b in range(1,4):
        for c in range(1,4):
            instancia = 'Instancia3D-' + str(i) + '-Tipo-' + str(b) + '-Ocupacao-' + str(c) + '.mat'
            i += 1
            print("\nInstancia: %s" % instancia)
            data = loadmat(instancia)
            patios, navio, porto_dict, Num_portos = CreateData(data)

            if i == 29 or i == 30 or i == 20 or i == 21:
                navio.append(navio[0].copy())
            if i == 31:
                navio.append(navio[0].copy())
                navio.append(navio[0].copy())
                navio.append(navio[0].copy())
                navio.append(navio[0].copy())

           # limite = 3
            tamanho_populacao = 10
            taxa_mutacao = 0.30
            taxa_crossover = 0.8
            numero_geracoes = 200
            NRr = 10  # numero de regras de retirada do patio
            NRc = 11  # numero de regras de carregamento
            NRd = 3   # numero de regras de descarregamento
            lbound = 1
            ubound = NRc*NRr*NRd  # total de combinação de regras

            #pool = multiprocessing.Pool(processes=4)
            start_time = time.time()
            ag = AlgoritmoGenetico(tamanho_populacao)
            resultado = ag.resolver(lbound, ubound, taxa_mutacao, numero_geracoes, patios, navio, porto_dict, Num_portos, start_time)
            end_time = (time.time() - start_time)
            #pool.close()
            #pool.join()

            lista_FO.append(ag.lista_num_movimentos)
            lista_Fitness.append(ag.lista_num_movimentos)
            solucao.append((resultado, ag.melhor_solucao.num_movimentos, end_time))


    # Graficos:
    linestyles = ['-', '--', '-.', ':']
    markerstyles = ['v', 'o', '.', ',', '1', '2', '3', '4',' ']
    ii = 28 # instancia
    kk = 1
    for k in range(len(lista_FO)):
        name = 'Instance ' + str(ii)
        plt.plot(lista_FO[k], label = name, ls = linestyles[kk]) #, marker = "v")
        ii += 1
        kk += 1
        if kk == 4:
            kk = 0
    plt.title('Objective Function Evolution')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Number of Relocations')
    plt.legend()
    plt.show()

    # for i in range(len(lista_Fitness)):
    #     name = 'Instance ' + str(i + 1)
    #     plt.plot(lista_FO[i], label = name)
    # plt.plot(ag.lista_solucoes)
    # plt.title('Fitness Evolution')
    # plt.xlabel('Number of Iterations')
    # plt.ylabel('Fitness Value')
    # plt.legend()
    # plt.show()

    df = pd.DataFrame(solucao,columns=['Individuo', 'Numero de Remanejamentos', 'Tempo de Execucao'])
    df['Regras'] = None
    for index, row in df.iterrows():
        individuo = row['Individuo']
        list = []
        for gene in individuo:
            Rr, Rc, Rd = NumToRules(gene, NRr, NRc, NRd)
            list.append((Rr, Rc, Rd))

        df['Regras'][index] = list

    list = []
    for dd in range(df.shape[0]):
        b = [i for sub in df['Regras'][dd] for i in sub]
        list.extend(b)

    count_map = {}
    for t in list:
        count_map[t] = count_map.get(t, 0) + 1
    ocorrencias_regras = pd.DataFrame.from_dict(count_map, orient='index')

    # nome_csv = instancia + 'solucao_mutacao_maior.csv'
    # df.to_csv(nome_csv, sep=';', index=False)
    #
    # nome_csv = instancia + '_ocorrencias_mutacao_maior.csv'
    # ocorrencias_regras.to_csv(nome_csv, sep=';')

    nome_excel = instancia + '_solucao.xlsx'
    df.to_excel(nome_excel, index=False)

    nome_excel = instancia + '_ocorrencias.xlsx'
    ocorrencias_regras.to_excel(nome_excel)
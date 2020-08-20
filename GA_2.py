import random
import matplotlib.pyplot as plt
from Regras import SimulaRegras
from scipy.io import loadmat
from CreateData import CreateData

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
                    Rd = 'Rr' + str(k + 1)
                    return Rr, Rc, Rd
                else:
                    counter += 1


class Individuo:
    def __init__(self, lbound, ubound, Num_portos, geracao=0):
        self.fitness = 0
        self.lbound = lbound
        self.ubound = ubound
        self.geracao = geracao
        self.cromossomo = []

        for i in range(Num_portos):
            self.cromossomo.append(random.randint(lbound, ubound))


    def avaliacao(self, patios, navio, porto_dict):
        # passar por todos os genes, simular cada um e obter o fitness final de cada individuo
        fitness = 0
        for i in range(len(self.cromossomo)):
            Rr, Rc, Rd = NumToRules(self.cromossomo[i], NRr, NRc, NRd)
            Rc='Rc9'
            Rr = 'Rr1'
            num_movimentos_total = SimulaRegras(i, patios[i], navio, porto_dict, Rr, Rc, Rd)
            fitness += num_movimentos_total

        self.fitness = fitness


    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))

        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]

        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos

    def mutacao(self, taxa_mutacao):
        # print("Antes %s " % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                random.randint(lbound, ubound)

        return self


class AlgoritmoGenetico:
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.num_movimentos = 0
        self.lista_solucoes = []

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
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo

    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.num_movimentos
        return soma

    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].num_movimentos
            pai += 1
            i += 1
        return pai

    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("Geração: %s -> Numero de Movimentos: %s Regra: %s" % (self.populacao[0].geracao,
                                                                     melhor.num_movimentos,
                                                                     melhor.cromossomo))

    def resolver(self, lbound, ubound, taxa_mutacao, numero_geracoes, patios, navio, porto_dict, Num_portos):
        self.inicializa_populacao(lbound, ubound, Num_portos)

        for individuo in self.populacao:
            individuo.avaliacao(patios, navio, porto_dict)

        self.ordena_populacao()   # ordenar a populacao por numero de movimentos de cada individuo
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)

        self.visualiza_geracao()

        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []

            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)

                filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))

            self.populacao = list(nova_populacao)

            for individuo in self.populacao:
                individuo.avaliacao()

            self.ordena_populacao()

            self.visualiza_geracao()

            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.nota_avaliacao)
            self.melhor_individuo(melhor)

        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.espaco_usado,
               self.melhor_solucao.cromossomo))

        return self.melhor_solucao.cromossomo


if __name__ == '__main__':

    data = loadmat('Instancia3D-1-Tipo-1-Ocupacao-1.mat')
    patios, navio, porto_dict, Num_portos = CreateData(data)
    limite = 3
    tamanho_populacao = 10
    taxa_mutacao = 0.01
    taxa_crossover = 0.8
    numero_geracoes = 100
    lbound = 1
    ubound = 510 # total de combinação de regras
    NRr = 10  # numero de regras de retirada do patio
    NRc = 17  # numero de regras de carregamento
    NRd = 3   # numero de regras de descarregamento
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(lbound, ubound, taxa_mutacao, numero_geracoes, patios, navio, porto_dict, Num_portos)


    # for valor in ag.lista_solucoes:
    #    print(valor)
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.show()


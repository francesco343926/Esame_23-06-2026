from database.dao import Dao
import networkx as nx

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._users_list = []
        #self.load_all_users()

        self.nbus= 0
        self.L= 0
        self.Ut= None

        self.nodes = []  # [obj]
        self.edges = dict()  # {(obj1, obj2)--> peso}
        self.map = dict()  # {id-oggetto --> obj}

        self.bestpath = []  # [(obj1, obj2, peso)]
        self.bestweight = 0.0

    """def load_all_users(self):
        self._users_list = Dao.read_all_users()
        print(f"Users: {self._users_list}")"""

    def creagrafo(self):
        self.nodes.clear()
        self.edges.clear()
        self.grafo.clear()
        self.map.clear()

        self.nodes = Dao.getnodes(self.nbus)  # [obj]
        self.grafo.add_nodes_from(self.nodes)

        for n in self.nodes:
            self.map[n.id] = n

        self.edges = Dao.getarchi(self.nodes, self.map, self.nbus)  # {(obj1, obj2)--> peso}
        archi = []
        for tupla in self.edges.items():
            r1 = tupla[0][0]
            r2 = tupla[0][1]
            p = tupla[1]
            archi.append((r1, r2, p))
        self.grafo.add_weighted_edges_from(archi)

    def getlista(self):     # [(obj, stren-fl)]
        lista = []
        for n in self.nodes:
            all_neigh = list(self.grafo.edges(n, data=True))  # [(nodo1, nodo2, {'weight'--> peso-float})]
            stren= 0
            for e in all_neigh:
                stren += e[2]["weight"]
            lista.append((n, stren))
        listaord = sorted(lista, key=lambda x: x[1], reverse=True)
        return listaord

    def cercapercorso(self):  # aggiorna attr bestpath [(obj1, obj2, peso)]
        self.bestpath.clear()
        self.bestweight = 0
        parz = [self.Ut]
        parz_edges = []  # (obj1, obj2, peso)
        self.ricorsione(parz, parz_edges)

    def ricorsione(self, parz, parz_edges):
        if self.contapeso(parz_edges) > self.bestweight:
            if len(parz) == self.L:
                self.bestpath = list(parz_edges)
                self.bestweight = self.contapeso(parz_edges)

        listaok = self.viciniammissibili(parz[-1], parz)  # [(obj, peso)]

        if len(parz) > self.L:
            return
        if len(listaok) == 0:
            return

        for v in listaok:
            parz_edges.append((parz[-1], v[0], v[1]))
            parz.append(v[0])
            self.ricorsione(parz, parz_edges)
            parz.pop()
            parz_edges.pop()

    def contapeso(self, parz_edges):
        tot = 0
        if len(parz_edges) == 0:
            return tot
        for tup in parz_edges:
            tot += tup[2]
        return tot

    def viciniammissibili(self, nodo, parz):  # [(obj, peso)]
        listaok = []
        all_neigh = list(self.grafo.edges(nodo, data=True))  # [(nodo1, nodo2, {'weight'--> peso-float})]
        for tupl in all_neigh:
            peso = tupl[2]["weight"]
            if tupl[1] not in parz:
                    listaok.append((tupl[1], peso))
        return listaok
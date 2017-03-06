#!/usr/bin/python3
#encoding: utf-8
"""Manipulação de sequencias de DNA utilizando o Igraph"""

from igraph import *
from bioanalise import Sequence

class IgraphSequence(Sequence):
    def get_graph(self, pass_length, subseq_length):
        pairs = self.get_sequence_pairs(pass_length, subseq_length)
        vertex = list()
        edges = list()
        #cont = 0
        excl = list()
        for cont in range(0, len(pairs) - 2, 1):
        #while cont < (len(pairs) - 2):
            if cont not in excl:
                pair_a = list(pairs[cont])
                pair_b = list(pairs[cont + 2])
                temp = set(set(set(pair_a) | set(pair_b)))

                dif = list(set(pair_a) ^ set(pair_b))
                sim = list(temp - set(dif))

                if len(sim) > 0:
                    if sim[0] not in vertex:
                        vertex.append(sim[0])

                for seq in dif:
                    if seq not in vertex:
                        vertex.append(seq)
                    if len(sim) > 0:
                        index_a = vertex.index(seq)
                        index_b = vertex.index(sim[0])
                        if [index_a, index_b] not in edges and [index_b, index_a] not in edges:
                            edges.append([vertex.index(seq), vertex.index(sim[0])])
                excl.append(cont)

        return Graph(vertex_attrs={"label": vertex}, edges=edges, directed=False)

    def plot_sequence(self, pass_length, subseq_length):
        pairs = self.get_sequence_pairs(pass_length, subseq_length)
        vertex = list()
        edges = list()
        #cont = 0
        excl = list()
        for cont in range(0, len(pairs) - 2, 1):
        #while cont < (len(pairs) - 2):
            if cont not in excl:
                pair_a = list(pairs[cont])
                pair_b = list(pairs[cont + 2])
                temp = set(set(set(pair_a) | set(pair_b)))

                dif = list(set(pair_a) ^ set(pair_b))
                sim = list(temp - set(dif))

                if len(sim) > 0:
                    if sim[0] not in vertex:
                        vertex.append(sim[0])

                for seq in dif:
                    if seq not in vertex:
                        vertex.append(seq)
                    if len(sim) > 0:
                        index_a = vertex.index(seq)
                        index_b = vertex.index(sim[0])
                        if [index_a, index_b] not in edges and [index_b, index_a] not in edges:
                            edges.append([vertex.index(seq), vertex.index(sim[0])])
                excl.append(cont)

        g = Graph(vertex_attrs={"label": vertex}, edges=edges, directed=False)
        plot(g)
    def print_adj_matrix(self, pass_length, subseq_length):
        pairs = self.get_sequence_pairs(pass_length, subseq_length)
        vertex = list()
        edges = list()
        #cont = 0
        excl = list()
        for cont in range(0, len(pairs) - 2, 1):
        #while cont < (len(pairs) - 2):
            if cont not in excl:
                pair_a = list(pairs[cont])
                pair_b = list(pairs[cont + 2])
                temp = set(set(set(pair_a) | set(pair_b)))

                dif = list(set(pair_a) ^ set(pair_b))
                sim = list(temp - set(dif))

                if len(sim) > 0:
                    if sim[0] not in vertex:
                        vertex.append(sim[0])

                for seq in dif:
                    if seq not in vertex:
                        vertex.append(seq)
                    if len(sim) > 0:
                        index_a = vertex.index(seq)
                        index_b = vertex.index(sim[0])
                        if [index_a, index_b] not in edges and [index_b, index_a] not in edges:
                            edges.append([vertex.index(seq), vertex.index(sim[0])])
                excl.append(cont)

        g = Graph(vertex_attrs={"label": vertex}, edges=edges, directed=False)
        matrix = g.get_adjacency()
        result = '\t' + '\t'.join(vertex) + "\n"
        for i in range(0, matrix.shape[0], 1):
            line = '\t'.join(str(x) for x in matrix[i])
            result += vertex[i] + '\t' + line + "\n"
        print(result)

        calc = RunningMean(matrix[2])
        print(calc.sd)


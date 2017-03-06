#!/usr/bin/python3
#encoding: utf-8
""" Manipula sequencias de DNA """
class Sequence(object):
    """Manipulação de sequencias"""
    #Método que inicializa o objeto
    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence
    #Método que retorna as subsequencias de acordo com os parâmetros
    def get_subsequences(self, pass_length, subseq_length):
        """Retorna uma lista com as sub-sequencias conforme parâmetros: passo e tamanho"""
        #Cria uma lista chamada 'sub_sequences'
        sub_sequences = list()
        #Varre a string 'sequence' do objeto avançando de acordo com o parâmetro 'pass_length'
        for i in range(0, len(self.sequence), pass_length):
            # Amazena na variável sub_sequence a substring iniciada com a posição atual do
            # contador('i') e terminada com o contador('i') mais o valor do parâmetro
            # 'subseq_length'
            sub_sequence = self.sequence[i:i+subseq_length]
            # Verifica se o tamanho da sub-sequencia =  igual ao valor de 'subseq_length'
            if len(sub_sequence) == subseq_length:
                # Adiciona 'sub_sequence' à lista 'sub_sequences'
                sub_sequences.append(sub_sequence)
        # Retorna a lista 'sub_sequences'
        return sub_sequences

    def get_sequence_pairs(self, pass_lenght, subseq_lenght):
        """Retorna uma lista com os pares de sub-sequencias conforme parâmetros: passo e tamanho"""
        pairs = list()
        for i in range(0, len(self.sequence) - (subseq_lenght + pass_lenght), pass_lenght):
            pair = [self.sequence[i:i + subseq_lenght], self.sequence[i + \
                subseq_lenght: (i + subseq_lenght) + subseq_lenght]]
            pairs.append(pair)
        return pairs

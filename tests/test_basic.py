import sys
import os
path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)

from bioanalise import IgraphSequence


SEQ = IgraphSequence("", "ATGGAGTCCAAA")

SEQ.plot_sequence(1,2)
#SEQ.print_adj_matrix(1,2)

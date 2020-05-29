from BCJR import BCJR
from util import *

p_mat = read_mat('test_data/AABC.csv')
bcjr1 = BCJR(p_mat, b=1)
bcjr1.remove_nonzero()
bcjr1.plot_sections(0,4)

p_mat = read_mat('test_data/ABBC.csv')
bcjr2 = BCJR(p_mat, b=1)
bcjr2.remove_nonzero()
bcjr2.plot_sections(0,4)

p_mat = read_mat('test_data/ABCC.csv')
bcjr3 = BCJR(p_mat, b=1)
bcjr3.remove_nonzero()
bcjr3.plot_sections(0,4)

p_mat = read_mat('test_data/Hypergraph.csv')
bcjr4 = BCJR(p_mat, b=1)
bcjr4.remove_nonzero()
bcjr4.plot_sections(0,5)
#p_mat = read_mat('test_data/file2.csv')
#bcjr2 = BCJR(p_mat, b=1)
#bcjr2.remove_nonzero()
#bcjr2.plot_sections(0,7)

#p_mat = read_mat('test_data/file3.csv')
#bcjr3 = BCJR(p_mat, b=2)
#bcjr3.remove_nonzero()
#bcjr3.plot_sections(0,5)

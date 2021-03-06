import csv
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def vex_connected( vex, edg ):
    edgs = []
    for v in vex:
        for e in edg:
            v0, a, v1 = e
            if np.array_equal(v0,v):
                edgs.append(v)
                break
    return edgs

def v2str( in_arr, i=None ):
    name = ""
    if i is not None: name += str(i) + '_'
    for s in in_arr:    
        name += str(int(s))
    return name

def arr2bistr( arr, dim ):
    bistr = ""
    for symbol in arr:
        for digit in symbol.value:
            bistr = bistr + str(int(digit))
    # print('bistr = ', bistr)
    return bistr

def in_list( vec_list, target ):
    for vec in vec_list:
        if np.array_equal(vec,target): return True
    return False

def read_mat( filename ):
    with open( filename, newline='') as f:
        reader = csv.reader(f)
        symbols = []
        for row in reader:
            rows = []
            for symbol in row:
                symbol_str = []
                for gf in symbol:
                    symbol_str.append(int(gf))
                rows.append(symbol_str)
            symbols.append(rows)
        rows_nparr = np.swapaxes( symbols, 0, 1 )
        size = int(int(rows_nparr.size)/len(symbols))
    return rows_nparr

def arr2int( v ):
    total = 0
    for e, digit in enumerate(v):
        total *= 2**digit.nbit
        total += int(digit)
    return total

def prmt_ply( nbit ):
    if nbit==1: return np.array([0,1])
    if nbit==2: return np.array([1,1,1])
    err_msg = "No primitive polynomial for nbit = ", str(nbit)
    raise ValueError(err_msg)

def fit_gfn( a, nbit ):
    b = prmt_ply(nbit)
    a = np.remainder(a,2)
    if a.size < b.size:
        return np.append( a, np.zeros(b.size-a.size-1, dtype=int) )
    while 1:
        if np.argwhere(a==1).size == 0:
            if a.size < b.size:
                return np.append( a, np.zeros(b.size-a.size-1, dtype=int) )
            else:
                return a[:b.size-1]
        msb = np.max(np.argwhere(a==1),axis=0)[0]
        if msb < len(b)-1:
            if a.size < b.size:
                return np.append( a, np.zeros(b.size-a.size-1, dtype=int) )
            else:
                return a[:b.size-1]
        remainder = np.append( b, np.zeros( msb - b.size + 1 ) )
        remainder = np.append( remainder, np.zeros(a.size - msb - 1))
        result = np.empty_like(a)
        for i, x in enumerate(result):
            result[i] = np.remainder( a[i]+remainder[i], 2)
        a = result

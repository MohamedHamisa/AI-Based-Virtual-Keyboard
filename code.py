#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**5) # used to set the maximum depth of the Python interpreter stack to the required limit.
def parent(n, st): # Fn to find set representative
    if n == st[n]:
        return n
    p = parent(st[n], st)
    st[n] = p # path compression
    return p

def kruskals(n, f, t, w):
    # Cases given for equal edge wt dont matter
    conn = []
    for i in range(len(f)):
        conn.append([w[i], f[i]-1, t[i]-1])
    conn.sort() # sort by edge weight
    s = [i for i in range(n)] # disjoint set
    ans = 0
    for wt, e1, e2 in conn:
        if parent(e1, s) != parent(e2, s): # If nodes are of different sets (no cycle)
            ans += wt
            s[parent(e1, s)] = parent(e2, s)
    print(ans)
    return str(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g_nodes, g_edges = map(int, input().rstrip().split())
    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())
    res = kruskals(g_nodes, g_from, g_to, g_weight)
    # Write your code here.
    fptr.write(res + '\n')
    fptr.close()



#
# blatantly stolen from phaethonprime.wordpress.com/2015/09/08/non-uniform-coupon-collectorsthe-problem/
#

import numpy as np
from itertools import combinations
from pprint import pprint
n = 14
ppr = 1/7*9/100
npr = 1/7*91/100
state_probs = {1:npr,2:npr,3:npr,4:npr,5:npr,6:npr,7:npr,8:ppr,9:ppr,10:ppr,11:ppr,12:ppr,13:ppr,14:ppr}
# state_probs = {k:1/n for k in range(1,n+1)}
n_states = 2**n
states = ['start']
T = np.zeros((n_states,n_states))
 
for k in range(1,n):
    for comb in combinations(range(1,n+1),k):
        states.append(comb)
        curr_ind = len(states) - 1
        if len(comb) == 1:
            prev_ind = 0
            T[prev_ind,curr_ind] += state_probs[comb[0]]
        else:
            for rem in comb:
                comb_prev = list(comb)
                comb_prev.remove(rem)
                idx = states.index(tuple(comb_prev))
                T[idx,curr_ind] += state_probs[rem]
        T[curr_ind,curr_ind] = sum(state_probs[x] for x in comb)
states.append((1,2,3,4,5,6,7,8,9,10,11,12,13,14))
T[-1,-1] = 1
comb = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
for a in states[-7:-1]:
    idx = states.index(a)
    comb_prev = list(comb)
    v = list(set(comb) - set(a))[0]
    T[idx,-1] = state_probs[v]

Q = T[:-1,:-1]
nt = Q.shape[0]
R = T[:-1,-1]
Ir = T[-1,-1]
It = np.eye(nt)
 
N = np.linalg.inv(It - Q)
t = np.dot(N,np.ones(nt))
tsq = t**2
t_var = np.dot(2*N - It,t) - tsq
 
# expected number of rolls is t[0]
print(t[0])

import math


def maxvertex(k, V, S):
    m = 0
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue
        if w[2] == 1:
            if m < w[0]:
                m = w[0]
                v = i
        else:
            if m < w[1]:
                m = w[1]
                v = i
        return v
def maxflow(T):
    w = [x[0] for x in T]
    return min(*w)


def updateV(V, T, f):
    for t in T:
        if t[1] == -1:
            continue
        sgn = V[t[2]][t[1]][2]
        V[t[1]][t[2]][0] -= f * sgn
        V[t[1]][t[2]][1] += f * sgn
        V[t[2]][t[1]][0] -= f * sgn
        V[t[2]][t[1]][1] += f * sgn
        
        
        
verticles = [[[2,2,2], [10,0,1], [0,0,1], [8,0,1], [0,0,1], [0,0,1], [0,0,1]],
    [[10,0,-1], [0,0,1], [5,0,1], [12,0,1], [10,0,1], [0,0,1], [6,0,1]],
    [[0,0,1], [8,0,-1], [0,0,1], [0,0,1], [5,0,-1], [5,0,1], [11,0,1]],
    [[8,0,-1], [13,0,-1], [0,0,1], [0,0,1], [4,0,1], [12,0,1], [0,0,1]],
    [[0,0,1], [10,0,-1], [5,0,1], [4,0,-1], [0,0,1], [6,0,-1], [9,0,1]],
    [[0,0,1], [0,0,1], [5,0,-1], [12,0,-1], [6,0,1], [0,0,1], [7,0,1]],
    [[0,0,1], [6,0,-1], [11,0,-1], [0,0,1], [9,0,-1], [7,0,-1], [0,0,1]]]
N = len(verticles)
init = 0 
end = 5
Tinit = (math.inf, -1, init)
f = []
j = init
while j != -1:
    k = init
    T = [Tinit]
    S = {init}
    while k != end:
        j = maxvertex(k, verticles, S)
        if j == -1:
            if k == init:
                break
            else:
                k = T.pop()[2]
                continue
        c = verticles[k][j][0] if verticles[k][j][2] == 1 else verticles[k][j][1]
        T.append((c, j, k))
        S.add(j)
        if j == end:
            f.append(maxflow(T))
            updateV(verticles, T, f[-1])
            break
        k = j
F = sum(f)
print(f"Від {init} до {end} максимальний потік дорівнює: = {F}")
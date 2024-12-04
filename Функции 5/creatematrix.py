def matrix(N=None, M=None, a=0):
    if N == None: N = 1
    if M == None: M = N
    matrix = [[a for i in range(M)] for j in range(N)]
    return matrix

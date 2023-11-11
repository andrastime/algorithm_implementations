# ITERATIVE APPROACH
def bin_search(A, t):
    if len(A) == 0:
        return -1
    
    l = 0
    r = len(A)

    m = (l + r) // 2
    
    while l < r:
        if t == A[m]:
            return m
        elif t < A[m]:
            r = m
        else:
            l = m + 1

        m = (l + r) // 2
            
    return -1

# RECURSIVE APPROACH
def bin_searchRec(A, t):
    return bin_searchAux(A, t, 0)

def bin_searchAux(A, t, offset):
    if len(A) == 0:
        return -1
    
    m = len(A) // 2

    if t == A[m]:
        return offset + m
    elif t < A[m]:
        return bin_searchAux(A[:m], t, offset)
    else:
        offset += m
        return bin_searchAux(A[m:], t, offset)

a = [1,3,6,45]

for i in a:
    print("Iterative Binary search:", bin_search(a, i), "Recursive:", bin_searchRec(a, i))

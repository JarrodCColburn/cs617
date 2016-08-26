def ConcaveMax(A, l, r):
    if l == r:  # only one element
        return A[l]
    else:
        m = (l + r) // 2  # find middle
        if A[m] > A[m + 1]:  # compare middle element with it's neighbor
            return ConcaveMax(A, l, m)  # look left half
        else:
            return ConcaveMax(A, m + 1, r)  #look right half

F = [0, 2, 5, 8, 13, 16, 20, 22, 23, 26, 25, 24, 17, 15, 12, 11, 9, 3]

def ConcaveMaxSimple(A):
    return ConcaveMax(A,0,len(A)-1)

print (ConcaveMaxSimple(F))

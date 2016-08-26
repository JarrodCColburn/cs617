def ConcaveMax(A, l, r): # defalt: l = 0, r = max index
    if l == r:
        return A[l]
    else:
        m = (l + r) // 2
        if A[m] > A[m + 1]:
            return ConcaveMax(A, l, m)  # go left
        else:
            return ConcaveMax(A, m + 1, r)  # go right

# Below used for testing:
# F = [0, 2, 5, 8, 13, 16, 20, 22, 23, 26, 25, 24, 17, 15, 12, 11, 9, 3]
# def ConcaveMaxSimple(A):
#    return ConcaveMax(A,0,len(A)-1)
# print (ConcaveMaxSimple(F))

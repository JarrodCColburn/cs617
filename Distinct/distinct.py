def distinct_simple(A):
    return distinct(A, 0, len(A)-1)


def distinct(A,i,n):
    if i == n:
        return 0
    else:
        x = int(A[i] == A[i+1])
        x += distinct(A,i+1,n)
    return x


F = [1,1,1,1,2,2]

print(distinct_simple(F))
# MaxSumArray runs in O(n^2)
def MSA4(A,i):
    if i == len(A)-1:
        return A[i]
    else:
        maxSum = MSA4(A,i+1)
        localSum = 0
        for j in range(i,len(A)):
            localSum += A[j]
            if localSum > maxSum:
                maxSum = localSum
    return maxSum

F = [13, -9, 5, -3, 2, 1, 6, -10, -23, 3]
#   4, 2, 9

print(MSA4(F,0))
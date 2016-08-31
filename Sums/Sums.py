# Givens:
#   a - number
#   A - array of numbers
# Solve:
#   (A[i], A[j]) - For all combinations of any two numbers in the array
#   Does there exist, such that:
#       A[i] + A[j] == a ?


def sums_recursive(A, a, l, r):
    if l == r:
        return False
    if a == A[l] + A[r]:
        return True
    if a < A[l] + A[r]:
        return sums_recursive(A, a, l, r - 1)
    else:
        return sums_recursive(A, a, l + 1, r)


def sum_iterative(A, a, l, r):
    while l < r:
        if a == A[l] + A[r]:
            return True
        elif a < A[l] + A[r]:
            r -= 1
        else:
            l += 1
    return False

F = [4, 7, 8, 11, 12, 19]

print(sums_recursive(F,25,0,len(F)-1))





def nondistinct_recursive(A, i, n):
    if i == n:                      # Is only last element remaining?
        return 0                    # If yes, no more pairs to examine.
    else:                           # If no, continue examining pairs.
        x = int(A[i] == A[i + 1])   # Is number same as its neighbor? If yes, increment one. If no, don't.
        x += unique_recursive(A, i + 1, n)  # Add to sum of neighbors.
        return x


def distinct_recursive(A, i, n):
    if i == n:
        return 1
    else:
        x = int(A[i] != A[i + 1])
        x += distinct_recursive(A, i + 1, n)
        return x


F = [1, 1, 1, 1, 2, 2, 3, 4, 4]


print(nondistinct_recursive(F, 0, len(F) - 1))

print(len(F))

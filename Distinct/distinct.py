def distinct_simple(A):
    return distinct(A, 0, len(A) - 1)


def distinct(A, i, n):
    if i == n:                      # Is only last element remaining?
        return 0                    # If yes, no more pairs to examine.
    else:                           # If no, continue examining pairs.
        x = int(A[i] == A[i + 1])   # Is number same as its neighbor? If yes, increment one. If no, don't.
        x += distinct(A, i + 1, n)  # Add to sum of neighbors
        return x


F = [1, 1, 1, 1, 2, 2, 3, 4, 4]

print(distinct_simple(F))

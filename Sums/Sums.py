# Givens:
#   a - number
#   A - array of numbers
# Solve:
#   (A[i], A[j]) - For all combinations of any two numbers in the array
#   Does there exist, such that:
#       A[i] + A[j] == a ?


def sums_simple(A, a):
    return sums_recursive(A, a, 0, len(A)-1)


def sums_recursive(A, a, i, j, f=True):
    if i == j:        # Only one element remains?
        return False  # If yes, couldn't find. :(

    if a == A[i] + A[j]:  # Do elements produce desired sum?
        return True       # If yes, found. :)

    if f:                                           # If examined right last time, examine left number this time.
        while a - A[i] < A[j]:                      # Are numbers on right relatively too large?
            j -= 1                                  # While yes, continue removing all too large from subset.
        return sums_recursive(A, a, i, j, not f)    # Once no, change focus to other side.

    else:                                           # If examined left last time, examine right this time.
        while A[i] < a - A[j]:                      # Are numbers on left relatively too low?
            i += 1                                  # While yes, continue removing all to low from subset.
        return sums_recursive(A, a, i, j, not f)    # Once no, change focus to other side.

F = [4, 7, 8, 11, 12, 20]

print(int(sums_simple(F, 24)))

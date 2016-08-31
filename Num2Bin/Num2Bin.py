# num2bin: int to bin converter
# Arg:
# n - any natural number
# Solve:
# Ret: binary equivalent
# Uses recursion
# Base-case: num2bin(0)


def num2bin(n):
    if n == 0:                      # Are no numbers remaining?
        return str("")              # If yes, done.
    else:                           # If no,
        x = str(num2bin(int(n / 2)))    # Find most significant figures.
        x += str(n % 2)             # Modulo 2, concatenate modulus as least significant digit.
    return str(x)  #


def num2comp(n, f=False):
    if n != 0:                      # Are no numbers remaining?
        x = str(num2comp(int(n / 2), (f and not bool(n % 2))))  # Find most significant figures.
        x += str(int((n < 0) ^ bool(n % 2)))  # Modulo 2, concatenate modulus as least significant digit.
        return str(x)        # If yes, done.
    else:                           # If no
        return str("")


def trial(n, f=False):
    if n==0:
        return ""
    if n > 0 or (f and bool(n % 2)):
        x = str(trial(int(n/2), False))

print(num2bin(40))
print(num2comp(40))
print(num2comp(-40))
print(num2comp(-40, True))


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

# Returns binary representation of an int


def any2comp(n, f=False):  # f: False for one's compliment, True for two's compliment. Doesn't effect positive numbers
    if n == 0:
        return str("")
    s = n <= 0  # s : signed number
    m = bool(n % 2)  # m : modulus
    x = str(any2comp(int(n / 2), f and s and not m))
    x += str(int((m and not s)  # Positive numbers.
                 or (f and m)  # Two's compliment correction of rightmost digits.
                 or (s and not f and not m)))  # One's compliment.
    return x


def pos2bin_iterative(n):
    x = str("")
    while n:
        x = str(int(bool(n % 2))) + x
        n = int(n / 2)
    return x


def neg2bin_1comp_iterative(n):
    x = str("")
    while n:
        x = str(int(not bool(n % 2))) + x
        n = int(n / 2)
    return x


def neg2bin_2comp_iterative(n):
    x = str("")
    while n:
        m = int(n % 2)  # Determine modulus.
        x = str(m) + x  # Cat modulus to left of string.
        n = int(n / 2)  # Reduce problem set.
        if bool(m):
            break
    return neg2bin_1comp_iterative(n) + x


def any2bin_iterative(n, f=False):
    x = "0b"
    if n > 0:
        return x + pos2bin_iterative(n)
    elif n < 0:
        if f:
            return x + neg2bin_2comp_iterative(n)
        else:
            return x + neg2bin_2comp_iterative(n)
    else:
        return x + "0"

print(any2bin_iterative(-45))

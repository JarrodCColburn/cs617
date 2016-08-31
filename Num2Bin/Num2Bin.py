# for all natural numbers convert int into binary

def num2bin(n):
    if n > 0:
        x = str(num2bin(n//2))
        x += str(n % 2)
        return str(x)
    else:
        return ""

print(num2bin(15))

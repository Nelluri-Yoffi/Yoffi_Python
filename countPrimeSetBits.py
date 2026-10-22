def count_prime_set_bits(left, right):
    def is_prime(x):
        if x < 2:
            return False
        for d in range(2, x):
            if x % d == 0:
                return False
        return True
    count = 0
    for num in range(left, right + 1):
        bits = bin(num).count("1")  
        if is_prime(bits):
            count += 1

    return count
print(count_prime_set_bits(6, 10)) 
import time
import random

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and coefficients."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    """Find modular inverse of e mod phi."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse doesn't exist")
    return x % phi

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_random_prime(lower_bound, upper_bound):
    """Generate a random prime number within the given range."""
    while True:
        candidate = random.randint(lower_bound, upper_bound)
        if is_prime(candidate):
            return candidate

def factor_modulus(N):
    """Factorize N into p and q assuming N = p * q."""
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return i, N // i
    return None, None

def main():
    for bit_length in [8, 16]:  # Test with 8-bit and 16-bit numbers
        lower_bound = 2 ** (bit_length // 2 - 1)
        upper_bound = 2 ** (bit_length // 2) - 1

        # Generate random primes p and q within the bounds for 8-bit or 16-bit modulus
        p = generate_random_prime(lower_bound, upper_bound)
        q = generate_random_prime(lower_bound, upper_bound)
        N = p * q
        phi = (p - 1) * (q - 1)

        # Choose a public exponent e
        e = random.randint(2, phi - 1)
        while extended_gcd(e, phi)[0] != 1:
            e = random.randint(2, phi - 1)

        # Measure factorization runtime
        start_time = time.perf_counter()
        p_fact, q_fact = factor_modulus(N)
        factorization_time = time.perf_counter() - start_time

        if p_fact is None or q_fact is None:
            print(f"Failed to factor modulus for {bit_length}-bit test.")
            continue

        # Calculate private exponent and measure runtime
        start_time = time.perf_counter()
        d = mod_inverse(e, phi)
        mod_inverse_runtime = time.perf_counter() - start_time

        # Output results for current bit length test
        print(f"\nTesting with {bit_length}-bit modulus:")
        print(f"Modulus N: {N}")
        print(f"Bit length of N: {N.bit_length()}")
        print(f"Factorization: p = {p_fact}, q = {q_fact}")
        print(f"Factorization time: {factorization_time * 1000:.6f} ms")
        print(f"Private exponent d: {d}")
        print(f"Runtime (modular inverse): {mod_inverse_runtime * 1000:.6f} ms")

if __name__ == "__main__":
    main()

import random
import time
from math import gcd

def is_prime(n):
    """Check if a number is a prime number."""
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

def generate_prime(bits):
    """Generate a prime number with the given bit length."""
    while True:
        number = random.getrandbits(bits)
        if is_prime(number):
            return number

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the GCD and coefficients."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, phi):
    """Find the modular inverse of e modulo phi."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception("Modular inverse doesn't exist")
    return x % phi

def generate_rsa_keys(bits):
    """Generate RSA public and private keys."""
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    N = p * q
    phi = (p - 1) * (q - 1)

    # Choose a public exponent e
    e = 65537  # Commonly used value for e
    if gcd(e, phi) != 1:
        raise Exception("e must be coprime with phi")

    # Compute the private exponent d
    d = mod_inverse(e, phi)

    return N, e, d

def measure_key_generation(bits):
    """Measure the runtime of key generation for a given bit size."""
    start_time = time.perf_counter()
    N, e, d = generate_rsa_keys(bits)
    end_time = time.perf_counter()
    runtime = end_time - start_time
    return N, e, d, runtime

# Generate and time RSA keys for 8-bit and 16-bit sizes
bits_list = [8, 16]

for bits in bits_list:
    N, e, d, runtime = measure_key_generation(bits)
    print(f"\nBits: {bits}")
    print(f"Modulus N: {N}")
    print(f"Public Exponent e: {e}")
    print(f"Private Exponent d: {d}")
    print(f"Runtime: {runtime * 1000:.6f} milliseconds")


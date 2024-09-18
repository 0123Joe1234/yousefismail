import time

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and the coefficients x and y such that ax + by = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def mod_inverse(e, phi_n):
    """Find the modular inverse of e mod phi_n."""
    g, x ,z= extended_gcd(e, phi_n)
    if g == 1:
        return x % phi_n
    else:
        return False  # In case no modular inverse exists

def brute_force_d(e, phi_n):
    """Brute force approach to find d such that (d * e) % phi_n == 1."""
    for d in range(2, phi_n):
        if (d * e) % phi_n == 1:
            return d
    return None

def factorize(N):
    """Factorize N into p and q assuming N = p * q where p and q are prime."""
    for p in range(2, int(N ** 0.5) + 1):
        if N % p == 0:
            q = N // p #without reminder  example : 5.3 -> 5
            return p, q
    return None, None

def test_with_runtime(N, e):
    """Test the RSA decryption key generation for given N and e."""
    print(f"Testing with N={N} (bit-length: {N.bit_length()} bits)")

    # Factorize N to find p and q
    start_time = time.perf_counter() #for a higher percision (time)
    p, q = factorize(N)
    if not p or not q:
        print("Factorization failed.")
        return
    
    phi_n = (p - 1) * (q - 1)
   # factorization_runtime = time.perf_counter() - start_time

    # Calculate d using modular inverse
    start_time = time.perf_counter()
    d_mod_inverse = mod_inverse(e, phi_n)
    mod_inverse_runtime = time.perf_counter() - start_time

    # Calculate d using brute force
    start_time = time.perf_counter()
    d_brute_force = brute_force_d(e, phi_n)
    brute_force_runtime = time.perf_counter() - start_time

    # Output results
    print(f"Factorization: p={p}, q={q}")
    print(f"Private exponent d (calculated using modular inverse): {d_mod_inverse}")
    print(f"Private exponent d (brute force): {d_brute_force}")
    #print(f"Runtime (factorization): {factorization_runtime*1000:.6f} milliseconds")
    print(f"Runtime (modular inverse): {mod_inverse_runtime*1000:.6f} milliseconds")
    print(f"Runtime (brute force): {brute_force_runtime * 1000:.6f} milliseconds")
    print("-" * 50)

def main():
    # Test case for 8-bit RSA key
    N_8bit = 88   # Example 8-bit modulus, N = 8 * 11
    e_8bit = 4    # Example public exponent
    test_with_runtime(N_8bit, e_8bit)
    
    # Test case for 16-bit RSA key
    N_16bit = 3233  # Example 16-bit modulus, N = 61 * 53
    e_16bit = 17    # Example public exponent
    test_with_runtime(N_16bit, e_16bit)

if __name__ == "__main__":
    main()

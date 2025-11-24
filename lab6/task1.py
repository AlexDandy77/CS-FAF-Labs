# RSA signing implementation
from sympy import randprime
from math import gcd

# hashed Haval224,4 message
HAVAL_HEX = "52d6a51666a983266b648a120a30691c71747f725435c043d212814a"

# Convert hex hash to integer (decimal representation as required by lab)
h = int(HAVAL_HEX, 16)
print(f"HAVAL224,4 hash (hex): {HAVAL_HEX}")
print(f"HAVAL224,4 hash (decimal):{h}\n")

bits = 1536
p_rsa = randprime(2**(bits - 1), 2**bits)
q_rsa = randprime(2**(bits - 1), 2**bits)
while p_rsa == q_rsa:
    q_rsa = randprime(2**(bits - 1), 2**bits)

n = p_rsa * q_rsa
phi_n = (p_rsa - 1) * (q_rsa - 1)

# Standard public exponent
e = 65537
if gcd(e, phi_n) != 1:
    raise ValueError("e and phi(n) are not coprime. Regenerate primes.")

# Modular inverse for d
def modinv(a, m):
    """Iterative modular inverse (no recursion)."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

d = modinv(e, phi_n)

print(f"RSA modulus n bit length: {n.bit_length()} bits (>= 3072 required)")
print("\nRSA public key:")
print(f"  p = {p_rsa}")
print(f"  q = {q_rsa}")
print(f"  phi(n) = {phi_n}")
print(f"  n = {n}")
print(f"  e = {e}")
print("\nRSA private key:")
print(f"  d = {d}\n")

# ----- Signing -----
# Signature s = h^d mod n
s_rsa = pow(h, d, n)
print("RSA Signature:")
print(f"  s = h^d mod n = {s_rsa}\n")

# ----- Verification -----
# Compute v = s^e mod n and check v == h
v_rsa = pow(s_rsa, e, n)
print("RSA Verification:")
print(f" v = s^e mod n = {v_rsa}")
print(f" Expected h    = {h}")
print("  Verification result:", "SUCCESS ✅" if v_rsa == h else "FAILED ❌")

from sympy import randprime
from math import gcd

# 1. Helper functions
def modinv(a, mes):
    """Modular inverse using Extended Euclidean Algorithm"""
    def egcd(a, b):
        if b == 0:
            return 1, 0, a
        x1, y1, g = egcd(b, a % b)
        return y1, x1 - (a // b) * y1, g
    x, y, g = egcd(a, mes)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % mes

# 2. Generate RSA keys
print("Generating two 1024-bit primes...")
bits = 1024
p = randprime(2**(bits-1), 2**bits)
q = randprime(2**(bits-1), 2**bits)

while p == q:
    q = randprime(2**(bits-1), 2**bits)

n = p * q
phi = (p - 1) * (q - 1)
e = 65537

if gcd(e, phi) != 1:
    raise ValueError("e and phi(n) are not coprime")

d = modinv(e, phi)

print("\n--- Generated RSA Keys ---")
print(f"p = {p}")
print(f"q = {q}")
print(f"n (modulus) = {n}")
print(f"phi(n) = {phi}")
print(f"Public exponent e = {e}")
print(f"Private exponent d = {d}")
print("--------------------------\n")

# 3. Convert message to integer
message = "Pavlovschii Alexei"
m = int(message.encode('utf-8').hex(), 16)
print(f"Message: {message}")
print(f"Message as integer (m):\n{m}\n")

# 4. Encrypt
c = pow(m, e, n)
print(f"Ciphertext (c = m^e mod n):\n{c}\n")

# 5. Decrypt
m_recovered = pow(c, d, n)
print(f"Decrypted integer (m'):\n{m_recovered}\n")

# Convert integer back to text
hex_message = hex(m_recovered)[2:]
if len(hex_message) % 2 != 0:
    hex_message = '0' + hex_message
plaintext = bytes.fromhex(hex_message).decode('utf-8')

print(f"Decrypted text:\n{plaintext}\n")
print("✅ Verification:", "SUCCESS" if plaintext == message else "FAILED")
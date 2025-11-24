# ElGamal signing implementation
import secrets
from math import gcd

# Modular inverse for d
def modinv(a, m):
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

# 1. Given parameters
p_elg = int("""
32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
""".strip())

g = 2  # generator

# hashed Haval224,4 message
HAVAL_HEX = "52d6a51666a983266b648a120a30691c71747f725435c043d212814a"

# Convert hex hash to integer (decimal representation as required by lab)
h = int(HAVAL_HEX, 16)
print(f"HAVAL224,4 hash (hex): {HAVAL_HEX}")
print(f"HAVAL224,4 hash (decimal):{h}\n")

print(f"ElGamal parameters:")
print(f"  p (2048-bit prime) = {p_elg}")
print(f"  g (generator)      = {g}\n")

# ----- Key generation -----
# Private key x in [2, p-2]
x = secrets.randbelow(p_elg - 2) + 2
y = pow(g, x, p_elg)

print("ElGamal keys:")
print(f"  Private key x = {x}")
print(f"  Public key y  = g^x mod p = {y}\n")

# ----- Signature generation -----
# ElGamal signature uses h mod (p-1)
h_mod = h % (p_elg - 1)

# Choose random k with gcd(k, p-1) = 1
k = secrets.randbelow(p_elg - 2) + 2
while gcd(k, p_elg - 1) != 1:
    k = secrets.randbelow(p_elg - 2) + 2

r = pow(g, k, p_elg)  # r = g^k mod p
k_inv = modinv(k, p_elg - 1)
s = ( (h_mod - x * r) * k_inv ) % (p_elg - 1) # s = (h - x*r) * k^(-1) mod (p-1)

print("ElGamal signature:")
print(f"  k (random, gcd(k, p-1)=1) = {k}")
print(f"  r = g^k mod p             = {r}")
print(f"  s = (h - x*r) * k^(-1) mod (p-1) = {s}")
print(f"  h_mod = h mod (p-1) = {h_mod}\n")
print(f"Signature = (r, s)\n")

# ----- Signature verification -----
# Check: g^h ≡ y^r * r^s (mod p)
left = pow(g, h_mod, p_elg)
right = (pow(y, r, p_elg) * pow(r, s, p_elg)) % p_elg

print("ElGamal verification:")
print(f"  Left  = g^h mod p               = {left}")
print(f"  Right = y^r * r^s mod p         = {right}")
print("  Verification result:", "SUCCESS ✅" if left == right else "FAILED ❌")
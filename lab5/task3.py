import secrets
import hashlib

# 1. Given parameters
p = int("""
32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
""".strip())

g = 2  # generator

# 2. Private keys
a = secrets.randbelow(p - 2) + 2  # Alice's private key
b = secrets.randbelow(p - 2) + 2  # Bob's private key

# 3. Public keys
A = pow(g, a, p)  # Alice sends this
B = pow(g, b, p)  # Bob sends this

# 4. Shared secret computation
S_alice = pow(B, a, p)
S_bob = pow(A, b, p)

assert S_alice == S_bob, "Error: Shared secrets do not match!"
shared_secret = S_alice

# 5. Derive AES-256 key
# Convert shared secret to bytes
shared_secret_bytes = shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, 'big')

# Derive a 256-bit AES key using SHA-256
aes_key = hashlib.sha256(shared_secret_bytes).digest()

# 6. Output results
print("\n--- Diffie-Hellman Key Exchange ---")
print(f"p (prime, 2048 bits) = {p}")
print(f"g (generator) = {g}")

print(f"\nAlice's private key (a): {a}")
print(f"Alice's public key (A = g^a mod p): {A}")

print(f"\nBob's private key (b): {b}")
print(f"Bob's public key (B = g^b mod p): {B}")

print(f"\nShared secret (S): {shared_secret}")

print(f"\nDerived AES-256 key (SHA-256 of S): {aes_key.hex()}")
print("------------------------------------\n")
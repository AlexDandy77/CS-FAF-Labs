import secrets

# 1. Given parameters
p = int("""
32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
""".strip())

g = 2  # generator

# 2. Key generation
a = secrets.randbelow(p - 2) + 2  # private key a
y = pow(g, a, p)                  # public key y = g^x mod p

print("\n--- ElGamal Key Generation ---")
print(f"p (prime, 2048 bits) = {p}")
print(f"g (generator) = {g}")
print(f"Private key a = {a}")
print(f"Public key y = {y}")
print("------------------------------\n")

# 3. Convert message to integer
message = "Pavlovschii Alexei"
m = int(message.encode('utf-8').hex(), 16)
if m >= p:
    raise ValueError("Message too large for modulus p")

print(f"Message: {message}")
print(f"Message as integer (m):\n{m}\n")

# 4. Encryption
k = secrets.randbelow(p - 2) + 2  # random session key
c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

print("--- Encryption ---")
print(f"Random k = {k}")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print("------------------\n")

# Ciphertext = (c1, c2)
ciphertext = (c1, c2)

# 5. Decryption
# Compute s = c1^x mod p
s = pow(ciphertext[0], a, p)

s_inv = pow(s, -1, p)
m_recovered = (ciphertext[1] * s_inv) % p

# 6. Convert back to text
hex_message = hex(m_recovered)[2:]
if len(hex_message) % 2 != 0:
    hex_message = '0' + hex_message
plaintext = bytes.fromhex(hex_message).decode('utf-8', errors='ignore')

print("--- Decryption ---")
print(f"s = {s}")
print(f"s⁻¹ mod p = {s_inv}")
print(f"Recovered m' = {m_recovered}")
print(f"Recovered text = {plaintext}")
print("------------------\n")

# 7. Verification
print("✅ Verification:", "SUCCESS" if plaintext == message else "FAILED")
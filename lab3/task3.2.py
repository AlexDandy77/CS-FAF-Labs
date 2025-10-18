RO_ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
ALPHABET_SIZE = len(RO_ALPHABET)
IDX = {ch: i for i, ch in enumerate(RO_ALPHABET)}

def normalize_text(s: str) -> str:
    return "".join(ch for ch in s.replace(" ", "")).upper()

def is_valid_ro_string(s: str) -> bool:
    return all(ch in RO_ALPHABET for ch in s)

def suggest_allowed_range():
    print("Allowed characters are only letters (A–Z or a–z) from the Romanian alphabet,")
    print("including diacritics: Ă, Â, Î, Ș, Ț. No digits, punctuation, or other symbols.")

def validate_key(key: str) -> bool:
    key_norm = normalize_text(key)
    if len(key_norm) < 7:
        print("Error: Key length must be at least 7 letters.")
        return False
    if not is_valid_ro_string(key_norm):
        print("Error: Key contains invalid characters for the Romanian alphabet.")
        suggest_allowed_range()
        return False
    return True

def extend_key(key_norm: str, length: int) -> str:
    if length == 0:
        return ""
    repeats, extra = divmod(length, len(key_norm))
    return key_norm * repeats + key_norm[:extra]

def vigenere_encrypt(plain: str, key: str) -> str:
    if not plain:
        return ""

    kx = extend_key(key, len(plain))
    out = []
    for pc, kc in zip(plain, kx):
        pi = IDX[pc]
        ki = IDX[kc]
        ci = (pi + ki) % ALPHABET_SIZE
        out.append(RO_ALPHABET[ci])
    return "".join(out)

def vigenere_decrypt(cipher: str, key: str) -> str:
    if not cipher:
        return ""

    kx = extend_key(key, len(cipher))
    out = []
    for cc, kc in zip(cipher, kx):
        ci = IDX[cc]
        ki = IDX[kc]
        pi = (ci - ki) % ALPHABET_SIZE
        out.append(RO_ALPHABET[pi])
    return "".join(out)

def main():
    print("--- Vigenere Cipher (RO alphabet, 31 letters) ---")
    print("Alphabet order:", RO_ALPHABET)
    while True:
        print("\n-- Main Menu --")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        option = input("Choose an option: ").strip()

        if option == "3":
            print("Exiting the program.")
            break
        elif option not in ("1", "2"):
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        key = input("Enter key (≥7 letters, Romanian alphabet): ").strip()
        if not validate_key(key):
            print("Error: Key must be at least 7 letters long and contain only Romanian letters.")
            continue

        text = input("Enter message/cryptogram (letters only; spaces allowed): ").strip()
        if not all((ch.isalpha() or ch.isspace()) for ch in text):
            print("Error: Only letters (A–Z or a–z, including Ă Â Î Ș Ț) and spaces are allowed.")
            suggest_allowed_range()
            continue

        text_norm = normalize_text(text)
        key_norm = normalize_text(key)
        if not is_valid_ro_string(text_norm) or not is_valid_ro_string(key_norm):
            print("Error: Input contains characters outside the Romanian alphabet after normalization.")
            suggest_allowed_range()
            continue

        try:
            if option == "1":
                result = vigenere_encrypt(text_norm, key_norm)
                print("Encrypted text:", result)
            else:
                result = vigenere_decrypt(text_norm, key_norm)
                print("Decrypted text:", result)
        except ValueError as e:
            print("Error:", e)
            continue

if __name__ == "__main__":
    main()
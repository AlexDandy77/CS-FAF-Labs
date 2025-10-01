BASE_TABLE = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def validate_k1(k1: int) -> bool:
    return 1 <= k1 <= 25

def validate_k2(k2: str) -> bool:
    return k2.isalpha() and len(k2) >= 7

def build_permuted_alphabet(k2: str) -> list[str]:
    k2 = k2.upper()
    seen = set()
    perm = []
    for ch in k2:
        if ch not in seen:
            perm.append(ch)
            seen.add(ch)
    for ch in BASE_TABLE:
        if ch not in seen:
            perm.append(ch)
            seen.add(ch)
    return perm

def preprocess_text(text: str) -> str:
    return text.upper().replace(" ", "")

def caesar_with_k2(text: str, k1: int, perm_alphabet: list[str], decrypt: bool = False) -> str:
    n = len(perm_alphabet)
    index_map = {ch: i for i, ch in enumerate(perm_alphabet)}
    out = []
    for ch in text:
        idx = index_map[ch]
        if decrypt:
            new_idx = (idx - k1) % n
        else:
            new_idx = (idx + k1) % n
        out.append(perm_alphabet[new_idx])
    return "".join(out)

def main():
    print("--- Caesar Cipher with 2 Keys (A-Z) ---")
    while True:
        print("\n-- Main Menu Options --")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        option = input("Choose an option: ").strip()

        if option == "3":
            print("Exiting program.")
            break
        elif option not in ("1", "2"):
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        try:
            k1 = int(input("Enter key 1 (1-25): ").strip())
        except ValueError:
            print("Error: Key 1 must be a number between 1 and 25.")
            continue
        if not validate_k1(k1):
            print("Error: Key 1 must be between 1 and 25.")
            continue

        k2 = input("Enter key 2 (Latin letters, length ≥ 7): ").strip()
        if not validate_k2(k2):
            print("Error: Key 2 must contain only letters and length ≥ 7.")
            continue

        text = input("Enter message/cryptogram (letters A-Z or a-z): ").strip()
        if not all(ch.isalpha() or ch == " " for ch in text):
            print("Error: Only letters A–Z or a–z (and spaces) are allowed.")
            continue

        clean_text = preprocess_text(text)
        perm_alphabet = build_permuted_alphabet(k2)

        if option == "1":
            result = caesar_with_k2(clean_text, k1, perm_alphabet, decrypt=False)
            print("Encrypted text:", result)
        else:
            result = caesar_with_k2(clean_text, k1, perm_alphabet, decrypt=True)
            print("Decrypted text:", result)

if __name__ == "__main__":
    main()
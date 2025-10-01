TABLE = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
INDEX = {ch: i for i, ch in enumerate(TABLE)}

def validate_key_str(s: str) -> int | None:
    s = s.strip()
    if not s.isdigit():
        return None
    k = int(s)
    return k if 1 <= k <= 25 else None

def is_az_letter(ch: str) -> bool:
    return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

def validate_text(text: str) -> bool:
    return all(is_az_letter(ch) or ch == ' ' for ch in text)

def preprocess_text(text: str) -> str:
    return text.upper().replace(" ", "")

def caesar_encrypt(text: str, key: int) -> str:
    out = []
    for ch in text:
        idx = INDEX[ch]
        out.append(TABLE[(idx + key) % 26])
    return "".join(out)

def caesar_decrypt(text: str, key: int) -> str:
    out = []
    for ch in text:
        idx = INDEX[ch]
        out.append(TABLE[(idx - key) % 26])
    return "".join(out)

def handle_action(action_name: str, transform_cb):
    key_raw = input("Enter key (1-25): ")
    key = validate_key_str(key_raw)
    if key is None:
        print("Error: Key must be a number between 1 and 25.")
        return

    prompt = "Enter message (letters only A-Z or a-z): " if action_name == "Encrypt" \
             else "Enter cryptogram (letters only A-Z or a-z): "
    text = input(prompt)
    if not validate_text(text):
        print("Error: Only letters A–Z or a–z (and spaces) are allowed.")
        return

    clean = preprocess_text(text)
    if not all(ch in INDEX for ch in clean):
        print("Error: Only letters A–Z or a–z are allowed.")
        return

    result = transform_cb(clean, key)
    label = "Encrypted text" if action_name == "Encrypt" else "Decrypted text"
    print(f"{label}: {result}")

def main():
    print("--- Caesar Cipher (A-Z) ---")
    while True:
        print("\nMain Menu Options:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        option = input("Choose an option: ").strip()

        if option == "1":
            handle_action("Encrypt", caesar_encrypt)
        elif option == "2":
            handle_action("Decrypt", caesar_decrypt)
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
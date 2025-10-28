import random
import string

PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]


def str_to_bitstring(k: str) -> str:
    if len(k) != 8:
        raise ValueError("DES key must be exactly 8 characters long (64 bits).")
    for c in k:
        if ord(c) > 127:
            raise ValueError(f"Non-ASCII character detected: {c!r}")
    return ''.join(f'{ord(c):08b}' for c in k)


def remove_parity_bits(bits64: str) -> str:
    return ''.join(bits64[i:i+7] for i in range(0, 64, 8))


def apply_pc1(bits64: str) -> str:
    return ''.join(bits64[i-1] for i in PC1)


def des_key_to_k_plus(k: str):
    print(f"Original key:\n{k}\n")
    bits64 = str_to_bitstring(k)
    print(f"64-bit key (with parity):\n{bits64}\n")

    bits56 = remove_parity_bits(bits64)
    print(f"After removing parity bits (56 bits):\n{bits56}\n")

    k_plus = apply_pc1(bits64)
    print(f"K+ after PC-1 permutation (56 bits):\n{k_plus}")
    print(f"K+ in hex: {hex(int(k_plus, 2))}")

def main():
    print("--- DES Key to K+ ---")
    while True:
        print("Select the method:")
        print("1. Manual")
        print("2. Random")
        print("3. Exit")
        option = input("Choose an option: ").strip()

        if option == "3":
            print("Exiting the program.")
            break
        elif option not in ("1", "2"):
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        try:
            if option == "1":
                key = input("Enter 8-character DES key: ")
                des_key_to_k_plus(key)
            else:
                key = ''.join(random.choices(string.printable, k=8))
                des_key_to_k_plus(key)
        except ValueError as e:
            print("Error:", e)
            continue


if __name__ == "__main__":
    main()
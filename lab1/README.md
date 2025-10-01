# Caesar Cipher — Lab 1 Tasks 1.1–1.3

This README describes how the **Caesar Cipher** tasks work, based on the lab requirements.

---

## Task 1.1 — Caesar Cipher with Single Key

**Objective:** Implement the Caesar algorithm for the English alphabet with a numeric key.

### Rules:
- **Key (k1):** an integer between **1 and 25**.
- **Input:** only letters `A–Z` or `a–z`. Other characters are not allowed.
- **Preprocessing:**
  - Convert all input text to **uppercase**.
  - Remove all spaces.
- **Encryption:** shift each letter forward by `k1` positions in the alphabet.
- **Decryption:** shift each letter backward by `k1` positions.

**Example:**
- Input: `HELLO WORLD`, k1 = 3
- Preprocessed: `HELLOWORLD`
- Encrypted: `KHOORZRUOG`
- Decrypted: `HELLOWORLD`

---

## Task 1.2 — Caesar Cipher with Two Keys (Permutation)

**Objective:** Improve Caesar’s security by using two keys.
- **Key 1 (k1):** integer in range [1..25].
- **Key 2 (k2):** keyword containing only Latin letters, length ≥ 7.

### How it works:
1. **Build permuted alphabet using k2:**
   - Place letters of `k2` at the start, without duplicates.
   - Append the rest of the alphabet A–Z in natural order, skipping letters already used.
   - Example: k2 = `CRYPTOGRAPHY` → alphabet becomes `C R Y P T O G A H B D E F I J K M L N Q S U V W X Z`.

2. **Apply Caesar shift (k1):**
   - Encryption: shift letters by +k1 positions in the permuted alphabet.
   - Decryption: shift letters by –k1 positions in the permuted alphabet.

**Example:**
- Message: `BRUTEFORCEATTACK`
- k1 = 3, k2 = `CRYPTOGRAPHY`
- Encrypted: `GTYZIAVWZAKKZFE`
- Decrypted: `BRUTEFORCEATTACK`

---

## Task 1.3 — Pair Exercise

**Objective:** Practice using Caesar + permutation cipher in pairs.

### Steps:
1. Each student chooses:
   - A message of **7–10 uppercase letters, no spaces** (e.g., `DEFENDAT`).
   - Keys: k1 (1–25) and k2 (keyword ≥ 7 letters).
2. Encrypt the message and produce a cryptogram.
3. Exchange with your partner: share **cryptogram + k1 + k2**.
4. Each partner decrypts the cryptogram using the supplied keys.
5. Compare the decrypted text with the original message.

---


# Lab 4: Block Ciphers. DES Algorithm.

**Author:** Alexei Pavlovschii    
**Course:** Cryptography and Security  
**Language:** Python

---

## Overview
This project demonstrates how to generate the **DES permuted key (K⁺)** from a given 8-character (64-bit) DES key.  
It includes parity-bit removal and application of the **PC-1 permutation**, as defined by the DES standard.

---

## Theoretical Background
DES (Data Encryption Standard) uses a 64-bit key where every 8th bit is a parity bit.  
Only 56 bits are used for encryption.  
This program performs the following:

1. Converts an 8-character key into binary (64 bits)
2. Removes parity bits → 56 bits remain
3. Applies the **PC-1 (Permuted Choice 1)** table
4. Displays intermediate and final results (K⁺ in binary and hex)

---

## How It Works

### DES Key Structure

| Bits | Purpose |
|------|----------|
| 64 | Original key (8 × 8 bits) |
| 8  | Parity bits (one per byte) |
| 56 | Effective encryption key |

### PC-1 Table (Permuted Choice 1)

```
57, 49, 41, 33, 25, 17, 9, 1,
58, 50, 42, 34, 26, 18, 10, 2,
59, 51, 43, 35, 27, 19, 11, 3,
60, 52, 44, 36, 63, 55, 47, 39,
31, 23, 15, 7, 62, 54, 46, 38,
30, 22, 14, 6, 61, 53, 45, 37,
29, 21, 13, 5, 28, 20, 12, 4
```

This table defines which bits from the original 64-bit key are used and how they’re reordered to form **K⁺**.

### DES Key Generation
| Step | Description |
|------|--------------|
| 1 | Convert key to binary (8 chars → 64 bits) |
| 2 | Remove every 8th parity bit |
| 3 | Apply PC-1 permutation to get **K⁺** |
| 4 | Print results and hexadecimal form |

---

## Example Output

```
--- DES Key to K+ ---
Select the method:
1. Manual
2. Random
3. Exit
Choose an option: 1
Enter 8-character DES key: 12345678

Original key:
12345678

64-bit key (with parity):
0011000100110010001100110011010000110101001101100011011100111000

After removing parity bits (56 bits):
00110000011001001100100110100011010001101100110110011100

K+ after PC-1 permutation (56 bits):
00000000000000001111111111110110011001111000100000001111
K+ in hex: 0xfff667880f
```

---

## Random Key Example

When choosing option `2`, the program generates a random 8-character printable key automatically.

Example:
```
Choose an option: 2
Generated random key: 8F]hjZJx
```
Then it performs the same steps to calculate **K⁺**.

---

## Run Instructions

```bash
python lab4.0.py
```

Then select:
- **1** to enter your own 8-character DES key
- **2** to generate a random printable 8-character key
- **3** to exit

---

> This lab demonstrates understanding of the DES key scheduling process, focusing on how the 64-bit input key is reduced and permuted to produce the 56-bit key K⁺ used in DES round key generation.

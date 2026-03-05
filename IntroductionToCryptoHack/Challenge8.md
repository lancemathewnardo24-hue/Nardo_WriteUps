## Challenge 8

>🔐 Encoding Messages as Integers (RSA Preprocessing)


![Alt text](Images/Chall7.png)

---
Perfect 👍 here’s a **simple, clean write-up** you can submit or keep in your notes.

---

# 📝 Challenge Write-Up

## 🔐 XOR Starter

---

## 📌 Challenge Summary

The challenge explains the XOR (⊕) operation and asks us to:

* Take the string `"label"`
* XOR each character with the integer `13`
* Convert the result back to a string

---

## 🧠 Concept Explanation

### What is XOR?

XOR (exclusive OR) is a bitwise operation:

| A | B | Output |
| - | - | ------ |
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 0      |

Important rule:

> XOR returns **1 if bits are different**, and **0 if they are the same**.

For numbers, XOR works on their binary form.

Example:

```
5 ^ 3
0101
0011
----
0110 = 6
```

---

## 🔑 Important Property of XOR

XOR is reversible:

```
A ^ B ^ B = A
```

This means if you XOR something twice with the same key, you get the original value back.

That is why XOR is commonly used in simple encryption schemes.

---

## 🛠 Tools Used

For this challenge, we used:

* Python
* `pwntools` library
* `xor()` function from pwntools

Import used:

```python
from pwn import xor
```

---

## 💻 Solution Code

```python
from pwn import xor

result = xor(b"label", 13)
print(result.decode())
```

Understanding XOR is foundational for learning cryptography.

---

here is the code I made for this challenge: 
[Open Challenge 7 code](Resources/chall7.py)

the flag is:
>ccrypto{x0r_i5_ass0c1at1v3}

[← Previous Challenge](Challenge7.md) | [Next Challenge →](Challenge9.md)
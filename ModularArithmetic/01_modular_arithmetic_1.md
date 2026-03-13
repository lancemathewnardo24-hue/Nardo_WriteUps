# Challenge: Modular Arithmetic 1

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Easy  
**URL:** https://cryptohack.org/courses/modular/ma1/

---

## 📖 Theory

The **modulo operation** finds the remainder after division.

```
a mod n = r   where   a = q * n + r,   0 ≤ r < n
```

Every integer has a **residue** modulo `n`. Two numbers are **congruent** modulo `n` if they share the same residue:

```
a ≡ b (mod n)   ⟺   n divides (a - b)
```

Key properties:
- `(a + b) mod n = ((a mod n) + (b mod n)) mod n`
- `(a * b) mod n = ((a mod n) * (b mod n)) mod n`
- The **canonical representative** is always in `[0, n-1]`

---

## 🧩 Challenge

Find the **smaller** of the two residues for the given values:
- `11 ≡ x (mod 6)` → what are the two canonical residues?

The challenge asks you to compute `a mod n` for two expressions and return the **smaller** result.

---

## 💡 Hints

- Use Python's `%` operator: `a % n`
- Both residues will be in range `[0, n-1]`
- The answer is simply: `min(a % n, b % n)`

---

## ✅ Solution

```python
a = 11 % 6
b = 8146798528947  # example value
n = 17  # example modulus

result = min(a, b % n)
print(result)
```

> **Note:** The actual numbers differ on the site. Apply the same logic.

---

## 🔑 Key Takeaway

Modular arithmetic is the foundation of almost all cryptographic systems. Every RSA, ECC, and DH operation reduces back to `mod n`.

# Challenge: Modular Arithmetic 2

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Easy  
**URL:** https://cryptohack.org/courses/modular/ma2/

---

## 📖 Theory

### Fermat's Little Theorem

If `p` is **prime** and `gcd(a, p) = 1`, then:

```
a^(p-1) ≡ 1 (mod p)
```

This means:
```
a^p ≡ a (mod p)
```

### Multiplicative Inverses

Because `a^(p-1) ≡ 1 (mod p)`, we can write:
```
a * a^(p-2) ≡ 1 (mod p)
```
So: **`a^(p-2) mod p`** is the modular inverse of `a`!

### Quadratic Residues

An integer `a` is a **quadratic residue** mod `p` if there exists `x` such that:
```
x^2 ≡ a (mod p)
```

For a prime `p`, exactly `(p-1)/2` nonzero elements are quadratic residues.

---

## 🧩 Challenge

The challenge gives you a prime `p` and asks you to compute:
```
a^b mod p
```
using Fermat's Little Theorem to simplify the exponent.

Reduce the exponent using:
```
a^b mod p  →  a^(b mod (p-1)) mod p
```

---

## 💡 Hints

- Python's built-in `pow(a, b, p)` is efficient for modular exponentiation
- Reduce huge exponents with `b % (p-1)` before computing
- If `b mod (p-1) == 0`, the answer is `1`

---

## ✅ Solution

```python
# pow(base, exp, mod) is optimized in Python
p = 101  # example prime
a = 273246787654  # example base
b = 65536         # example exponent

result = pow(a, b, p)
print(result)

# Alternative: reduce exponent first
reduced_exp = b % (p - 1)
result2 = pow(a, reduced_exp, p)
print(result2)
```

---

## 🔑 Key Takeaway

Fermat's Little Theorem is used constantly in RSA:
- Key generation relies on `a^(p-1) ≡ 1 (mod p)`
- Modular inverse via `pow(a, p-2, p)` is a clean Python one-liner
- Always use `pow(a, b, n)` — never compute `a**b` first (it will overflow/be slow)

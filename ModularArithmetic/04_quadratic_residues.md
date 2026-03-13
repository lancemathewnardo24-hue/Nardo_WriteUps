# Challenge: Quadratic Residues

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Medium  
**URL:** https://cryptohack.org/courses/modular/quadratic/

---

## 📖 Theory

### Quadratic Residues

An integer `a` is a **quadratic residue** mod `p` if:
```
∃ x : x^2 ≡ a (mod p)
```

For a prime `p`, there are exactly `(p-1)/2` quadratic residues in `{1, ..., p-1}`.

### Legendre Symbol

The **Legendre symbol** `(a/p)` tells you if `a` is a QR mod prime `p`:

```
(a/p) = a^((p-1)/2) mod p

Result:
  0  → a ≡ 0 (mod p)
  1  → a is a quadratic residue mod p
 -1  → a is a quadratic non-residue mod p
```

(Note: `-1 ≡ p-1 (mod p)`)

---

## 🧩 Challenge

Given a list of integers and a prime `p`, find which ones are **quadratic residues** mod `p`, then find the square root of one of them.

Steps:
1. Compute the Legendre symbol for each candidate
2. Identify which ones equal `1` (are QRs)
3. Find the square root using the **Tonelli-Shanks algorithm** (or shortcut below)

---

## 💡 Hints

- Legendre symbol: `pow(a, (p-1)//2, p)`
- If `p ≡ 3 (mod 4)`, square root is simply: `pow(a, (p+1)//4, p)`
- For general `p`, use Tonelli-Shanks
- `sympy.sqrt_mod(a, p)` also works

---

## ✅ Solution

```python
p = 29  # example prime
candidates = [14, 6, 11]  # example candidates

# Step 1: Find quadratic residues
qrs = [a for a in candidates if pow(a, (p-1)//2, p) == 1]
print("Quadratic residues:", qrs)

# Step 2: Find square root (shortcut for p ≡ 3 mod 4)
def sqrt_mod(a, p):
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    # General: Tonelli-Shanks
    return tonelli_shanks(a, p)

def tonelli_shanks(n, p):
    """Find x such that x^2 ≡ n (mod p)"""
    if pow(n, (p - 1) // 2, p) != 1:
        return None  # not a QR
    # Factor out powers of 2 from p-1
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    # Find a quadratic non-residue z
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while True:
        if t == 0: return 0
        if t == 1: return r
        i, tmp = 1, pow(t, 2, p)
        while tmp != 1:
            tmp = pow(tmp, 2, p)
            i += 1
        b = pow(c, pow(2, m - i - 1, p - 1), p)
        m, c, t, r = i, pow(b, 2, p), (t * pow(b, 2, p)) % p, (r * b) % p

for qr in qrs:
    root = sqrt_mod(qr, p)
    print(f"sqrt({qr}) mod {p} = {root}")
    assert pow(root, 2, p) == qr  # verify
```

---

## 🔑 Key Takeaway

Quadratic residues are central to:
- **RSA**: Jacobi/Legendre symbols used in primality testing
- **Rabin cryptosystem**: decryption requires computing square roots mod n
- **Zero-knowledge proofs**: QR-based protocols
- **Tonelli-Shanks** is the go-to algorithm for modular square roots

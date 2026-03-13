# Challenge: Discrete Logarithm

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Medium  
**URL:** https://cryptohack.org/courses/modular/discrete_log/

---

## 📖 Theory

### Discrete Logarithm Problem (DLP)

Given `g`, `h`, and `p`, find `x` such that:
```
g^x ≡ h (mod p)
```

Written as: `x = log_g(h) mod p`

This is **computationally hard** for large `p` — the basis of DH, DSA, ElGamal security.

### Baby-Step Giant-Step (BSGS)

Solves DLP in `O(√p)` time and space.

**Idea:** Write `x = i*m + j` where `m = ⌈√(p-1)⌉`

Then: `g^(i*m + j) = h` → `g^j = h * (g^(-m))^i`

Algorithm:
1. Precompute baby steps: `{g^j mod p : j = 0..m}` → store in dict
2. Compute giant steps: `h * (g^(-m))^i mod p` for `i = 0..m`
3. Find a collision → `x = i*m + j`

---

## 🧩 Challenge

Given `g`, `h`, and a small prime `p`, compute the discrete logarithm `x` such that `g^x ≡ h (mod p)`.

---

## 💡 Hints

- For small `p`, brute force works: `for x in range(p): if pow(g,x,p)==h`
- For medium `p`, use Baby-Step Giant-Step
- `sympy.ntheory.discrete_log(p, h, g)` solves it
- `sage`: `discrete_log(h, g)` in a multiplicative group

---

## ✅ Solution

```python
# Method 1: Brute force (small p only)
def brute_force_dlog(g, h, p):
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

# Method 2: Baby-Step Giant-Step
import math

def bsgs(g, h, p):
    m = math.isqrt(p) + 1
    # Baby steps: store g^j mod p
    table = {pow(g, j, p): j for j in range(m)}
    # Giant steps
    inv_gm = pow(pow(g, m, p), -1, p)  # (g^m)^(-1) mod p
    gamma = h
    for i in range(m):
        if gamma in table:
            return i * m + table[gamma]
        gamma = (gamma * inv_gm) % p
    return None

# Method 3: sympy
from sympy.ntheory.residues import n_order
from sympy.ntheory import discrete_log

g = 5
h = 8  # example: 5^x ≡ 8 (mod p)
p = 29 # example prime

x = discrete_log(p, h, g)
print(f"x = {x}")

# Verify
assert pow(g, x, p) == h
print("Verified!")

# BSGS example
x2 = bsgs(g, h, p)
print(f"BSGS: x = {x2}")
```

---

## 🔑 Key Takeaway

The DLP underpins a large chunk of modern crypto:
- **Diffie-Hellman** key exchange security relies on DLP hardness
- **DSA / ECDSA**: signing uses discrete log in `ℤₚ*` or on elliptic curves
- **Index Calculus**: breaks DLP in `O(exp(√(log p log log p)))` — reason we need 2048+ bit primes
- For CryptoHack, BSGS is often sufficient for challenges with small moduli

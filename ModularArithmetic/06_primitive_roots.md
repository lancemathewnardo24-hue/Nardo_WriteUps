# Challenge: Primitive Roots / Generators

**Category:** Mathematics > Modular Arithmetic  
**Difficulty:** Medium  
**URL:** https://cryptohack.org/courses/modular/primitive/

---

## 📖 Theory

### Multiplicative Groups

The set `ℤₙ* = {a : 1 ≤ a ≤ n-1, gcd(a,n)=1}` forms a **multiplicative group** under mod `n`.

Its size is `φ(n)` (Euler's totient function).

### Order of an Element

The **order** of `g` in `ℤₙ*` is the smallest positive integer `k` such that:
```
g^k ≡ 1 (mod n)
```

By Lagrange's theorem, `k` must divide `φ(n)`.

### Primitive Root / Generator

`g` is a **primitive root** mod `n` if its order equals `φ(n)`.
This means `g` **generates** the entire group — its powers hit every element:
```
{g^1, g^2, ..., g^φ(n)} = ℤₙ*
```

Primitive roots exist when `n` is: `1, 2, 4, p^k, or 2p^k` (for odd prime `p`).

### Finding Primitive Roots

`g` is a primitive root mod `p` iff for every prime factor `q` of `p-1`:
```
g^((p-1)/q) ≢ 1 (mod p)
```

---

## 🧩 Challenge

Given a prime `p`, find the **smallest primitive root** (generator) of `ℤₚ*`.

---

## 💡 Hints

- Factorize `p-1` to get its prime factors
- Test each `g = 2, 3, 4, ...` until one passes the primitive root test
- `sympy.ntheory.primitive_root(p)` finds it directly

---

## ✅ Solution

```python
from sympy import factorint, primitive_root

p = 28151  # example prime

# Method 1: sympy (easiest)
g = primitive_root(p)
print(f"Primitive root: {g}")

# Method 2: Manual
def is_primitive_root(g, p):
    phi = p - 1
    prime_factors = factorint(phi).keys()
    return all(pow(g, phi // q, p) != 1 for q in prime_factors)

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g

g_manual = find_primitive_root(p)
print(f"Manual: {g_manual}")

# Verify order = p-1
phi = p - 1
assert pow(g, phi, p) == 1
# No smaller exponent works
from sympy import factorint
for q in factorint(phi):
    assert pow(g, phi // q, p) != 1
print("Verified primitive root!")
```

---

## 🔑 Key Takeaway

Primitive roots power **discrete logarithm-based** cryptosystems:
- **Diffie-Hellman**: uses a generator `g` of a prime-order group
- **ElGamal**: encryption/signing uses powers of a generator
- **Discrete Log Problem (DLP)**: given `g^x mod p`, find `x` — this is hard!
- The security of DH depends on DLP being computationally infeasible

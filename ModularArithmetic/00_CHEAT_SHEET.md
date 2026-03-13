# 🔐 CryptoHack — Modular Arithmetic Cheat Sheet

---

## ⚡ Quick Reference Table

| Task | Python One-liner |
|------|-----------------|
| `a mod n` | `a % n` |
| Fast modular exponentiation | `pow(a, b, n)` |
| Modular inverse (prime modulus) | `pow(a, p-2, p)` |
| Modular inverse (general, Python 3.8+) | `pow(a, -1, n)` |
| Legendre symbol (is QR?) | `pow(a, (p-1)//2, p)` → 1=yes, p-1=no |
| Square root mod p (p ≡ 3 mod 4) | `pow(a, (p+1)//4, p)` |
| Find primitive root | `sympy.ntheory.primitive_root(p)` |
| Discrete log | `sympy.ntheory.discrete_log(p, h, g)` |
| Factorize n | `sympy.factorint(n)` |
| GCD | `math.gcd(a, b)` |
| Extended GCD | `gmpy2.gcdext(a, b)` |
| Order of element | `sympy.ntheory.n_order(a, n)` |
| Euler's totient φ(n) | `sympy.totient(n)` |

---

## 📐 Core Formulas

### Modular Arithmetic Properties
```
(a + b) mod n  =  ((a mod n) + (b mod n)) mod n
(a * b) mod n  =  ((a mod n) * (b mod n)) mod n
(a - b) mod n  =  ((a mod n) - (b mod n)) mod n  [can be negative, add n]
```

### Fermat's Little Theorem (p prime, gcd(a,p)=1)
```
a^(p-1) ≡ 1 (mod p)
a^p     ≡ a (mod p)
a^(-1)  ≡ a^(p-2) (mod p)
```

### Euler's Theorem (gcd(a,n)=1)
```
a^φ(n) ≡ 1 (mod n)
φ(p)   =  p - 1            (p prime)
φ(pq)  =  (p-1)(q-1)       (p, q distinct primes)
```

### Chinese Remainder Theorem
```
x ≡ aᵢ (mod nᵢ)  for pairwise coprime nᵢ
→  unique x mod N,  where N = Π nᵢ
```

### Legendre Symbol
```
(a/p) = a^((p-1)/2) mod p
      = 1   if a is a quadratic residue mod p
      = p-1 if a is a quadratic non-residue mod p
      = 0   if p | a
```

---

## 🐍 Essential Code Snippets

### Imports You'll Always Need
```python
import math
from sympy import factorint, isprime, totient
from sympy.ntheory import primitive_root, discrete_log
from sympy.ntheory.modular import crt
import gmpy2
```

### Extended GCD
```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def modinv(a, n):
    g, x, _ = extended_gcd(a % n, n)
    if g != 1:
        raise ValueError("No inverse")
    return x % n
```

### CRT (manual)
```python
def crt_solve(remainders, moduli):
    N = 1
    for n in moduli: N *= n
    x = 0
    for a, n in zip(remainders, moduli):
        Ni = N // n
        x += a * Ni * pow(Ni, -1, n)
    return x % N
```

### Baby-Step Giant-Step (Discrete Log)
```python
import math
def bsgs(g, h, p):
    m = math.isqrt(p) + 1
    table = {pow(g, j, p): j for j in range(m)}
    inv_gm = pow(pow(g, m, p), -1, p)
    gamma = h
    for i in range(m):
        if gamma in table:
            return i * m + table[gamma]
        gamma = gamma * inv_gm % p
    return None
```

### Tonelli-Shanks (Square Root mod p)
```python
def tonelli_shanks(n, p):
    if pow(n, (p-1)//2, p) != 1:
        return None
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2; s += 1
    z = next(z for z in range(2, p) if pow(z, (p-1)//2, p) == p-1)
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q+1)//2, p)
    while True:
        if t == 1: return r
        i, tmp = 1, pow(t, 2, p)
        while tmp != 1: tmp = pow(tmp, 2, p); i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b*b%p, t*b*b%p, r*b%p
```

### Quadratic Residue Check
```python
def is_quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1

def sqrt_mod(a, p):
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    return tonelli_shanks(a, p)
```

### Primitive Root Check
```python
from sympy import factorint
def is_primitive_root(g, p):
    phi = p - 1
    return all(pow(g, phi // q, p) != 1 for q in factorint(phi))
```

---

## 🔢 Number Theory Refresher

| Concept | Definition |
|---------|-----------|
| `gcd(a,b)` | Largest integer dividing both a and b |
| `lcm(a,b)` | `a*b // gcd(a,b)` |
| `φ(n)` | Count of integers in `[1,n]` coprime to `n` |
| `ord_n(a)` | Smallest `k > 0` such that `a^k ≡ 1 (mod n)` |
| Primitive root | Element with `ord_n(g) = φ(n)` |
| Quadratic residue | `a` for which `x^2 ≡ a (mod p)` has a solution |

---

## 📚 Useful Libraries

| Library | Install | Key Uses |
|---------|---------|----------|
| `sympy` | `pip install sympy` | factoring, DLP, primitives, totient |
| `gmpy2` | `pip install gmpy2` | fast big-int ops, `invert`, `is_prime` |
| `pycryptodome` | `pip install pycryptodome` | AES, RSA, hashes |
| `sage` (SageMath) | separate install | everything math |

---

## ⚠️ Common Gotchas

1. **Never use `a**b % n`** — Python computes the huge integer first. Always use `pow(a, b, n)`.
2. **Inverse only exists if `gcd(a,n) = 1`** — check first!
3. **Fermat's Little Theorem only works for prime `p`** — use Euler's theorem for composite `n`.
4. **Square roots mod p** — there are always **two** roots: `r` and `p-r`. The challenge may need the smaller one.
5. **CRT requires pairwise coprime moduli** — verify with `gcd(nᵢ, nⱼ) = 1`.
6. **Discrete log is only efficient for small `p`** — for large primes, use Index Calculus or Pohlig-Hellman.

---

## 🗺️ Challenge Map

```
Modular Arithmetic 1  → Basic mod, residues
Modular Arithmetic 2  → Fermat's Little Theorem
Modular Inverting     → pow(a,-1,p), Extended GCD
Quadratic Residues    → Legendre symbol, Tonelli-Shanks
CRT                   → Chinese Remainder Theorem
Primitive Roots       → Generators, order of elements
Discrete Logarithm    → Baby-Step Giant-Step (BSGS)
```
